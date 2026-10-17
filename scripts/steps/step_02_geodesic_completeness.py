#!/usr/bin/env python3
"""Step 02: verify the manuscript's conformal power-law geodesics.

On the stated static background, A(eta)=C eta**(-p). Null affine length
obeys d lambda/d eta=A**2. A timelike geodesic of conserved momentum q
obeys d tau/d eta=A**2/sqrt(A**2+q**2). Integrate finite segments in log eta
and check independent quadrature/closed forms. Infinite-end completeness
comes from the analytic integral criterion, never a finite numerical cutoff.
This verifies the specified background, not its dynamical generation.
"""
from pathlib import Path
import hashlib
import numpy as np
from scipy.integrate import solve_ivp, quad
from th_common import (TEPLogger, ensure_dirs, print_status, set_step_logger,
                       step_json_path, step_csv_path, write_json, write_csv)
from step_01_matter_frame_curvature import DEFAULT_P

STEP_ID = 'step_02_geodesic_completeness'


def power_integral(exponent, log_eta_ratio):
    """Integral of exp(exponent*x), stable at the logarithmic boundary."""
    if exponent == 0:
        return float(log_eta_ratio)
    return float(np.expm1(exponent * log_eta_ratio) / exponent)


def completeness_criterion(p, q=1.0):
    """Analytic infinite-end criterion in the manuscript's p>0 family."""
    if not np.isfinite(p) or p <= 0 or not np.isfinite(q):
        raise ValueError('Finite p>0 and finite conserved momentum required')
    return {'null_geodesics_complete': bool(p <= .5),
            'comoving_timelike_complete': bool(p <= 1.),
            'specified_timelike_complete': bool(p <= (1. if q == 0 else .5)),
            'all_timelike_geodesics_complete': bool(p <= .5)}


def integrate_profile(p=DEFAULT_P, q=1.0, eta_max=1e8, n_points=400,
                      C=1.0, rtol=2e-10):
    """Accumulate lambda, tau and radial coordinate, starting at eta=1."""
    criterion = completeness_criterion(p, q)
    if not np.isfinite(C) or C <= 0 or not np.isfinite(eta_max) or eta_max <= 1:
        raise ValueError('C>0 and finite eta_max>1 required')
    if n_points < 2:
        raise ValueError('At least two trajectory samples required')
    xmax = float(np.log(eta_max))
    x = np.linspace(0., xmax, n_points)

    def rhs(log_eta, _):
        eta = np.exp(log_eta)
        A = C * np.exp(-p * log_eta)
        norm = np.hypot(A, q)
        return [eta*A*A, eta*A*A/norm, eta*q/norm]

    sol = solve_ivp(rhs, (0., xmax), [0., 0., 0.], t_eval=x,
                    method='DOP853', rtol=rtol, atol=rtol*.01)
    if not sol.success or not np.all(np.isfinite(sol.y)):
        raise RuntimeError(f'Geodesic integration failed: {sol.message}')
    null_exact = C*C*power_integral(1-2*p, xmax)
    proper_quad, quad_error = quad(lambda t: rhs(t, None)[1], 0., xmax,
                                   epsabs=1e-10, epsrel=2e-11, limit=200)
    null_error = abs(sol.y[0,-1]-null_exact)/max(1., abs(null_exact))
    proper_error = abs(sol.y[1,-1]-proper_quad)/max(1., abs(proper_quad))
    if null_error > 5e-8 or proper_error > 5e-8:
        raise ArithmeticError('Geodesic integration failed independent parity')
    eta = np.exp(x)
    A = C*np.exp(-p*x)
    summary = {'p':float(p), 'q':float(q), 'C':float(C), 'eta_max':float(eta_max),
               'integration_success':True, 'solver_message':sol.message,
               'null_affine_length':float(sol.y[0,-1]),
               'proper_time':float(sol.y[1,-1]),
               'null_closed_form':null_exact,
               'proper_time_independent_quadrature':float(proper_quad),
               'quadrature_error_estimate':float(quad_error),
               'null_scaled_error':float(null_error),
               'timelike_scaled_error':float(proper_error),
               'infinite_end_criterion':criterion}
    if q == 0:
        exact = C*power_integral(1-p,xmax)
        summary['comoving_closed_form'] = exact
        if abs(sol.y[1,-1]-exact)/max(1.,abs(exact)) > 5e-8:
            raise ArithmeticError('Comoving closed-form check failed')
    rows=[{'eta':float(t), 'z':float(np.expm1(p*xx)), 'A_clock':float(a),
           'null_affine_parameter':float(lam), 'null_r':float(t-1.),
           'timelike_proper_time':float(tau), 'timelike_r':float(r)}
          for t,xx,a,lam,tau,r in zip(eta,x,A,*sol.y)]
    return summary, rows


def test_geodesic_completeness(z_max=1000., n_points=1000, p=DEFAULT_P, q=1., C=1.):
    """Validate the specified profile; z=(eta/eta0)**p-1 is a clock ratio."""
    if not np.isfinite(z_max) or z_max <= 0:
        raise ValueError('Positive finite redshift extent required')
    completeness_criterion(p,q)
    eta_max = float(np.exp(np.log1p(z_max)/p))
    result, rows = integrate_profile(p,q,eta_max,n_points,C)
    status = result['infinite_end_criterion']
    complete = status['null_geodesics_complete'] and status['all_timelike_geodesics_complete']
    return {'step':STEP_ID, 'description':__doc__,
            'parameters':{'p':p,'q':q,'C':C,'z_max':z_max,'eta_max':eta_max,'n_points':n_points},
            'null_geodesics':{'integration_success':True,
                'affine_parameter_complete':status['null_geodesics_complete'],
                'finite_segment_affine_length':result['null_affine_length']},
            'timelike_geodesics':{'integration_success':True,
                'proper_time_complete':status['specified_timelike_complete'],
                'all_timelike_geodesics_complete':status['all_timelike_geodesics_complete'],
                'finite_segment_proper_time':result['proper_time']},
            'completeness_status':{'null_geodesics_complete':status['null_geodesics_complete'],
                'timelike_geodesics_complete':status['all_timelike_geodesics_complete'],
                'geodesically_complete':bool(complete)},
            'validation':result,
            'claim_basis':'Analytic infinite-end integrability, independently checked on finite segments; no cutoff-based inference.',
            'interpretation':('The specified power-law branch is null and timelike complete.' if complete else
                'This p lies outside the null/all-timelike complete branch; the comoving criterion is reported separately.'),
            '_trajectory':rows}


def run():
    logger=TEPLogger(STEP_ID, log_file_path=Path(f'logs/{STEP_ID}.log'))
    set_step_logger(logger);ensure_dirs()
    result=test_geodesic_completeness()
    write_csv(step_csv_path(STEP_ID),result.pop('_trajectory'))
    # Include the logarithmic boundary and controls outside the selected branch.
    result['power_law_sensitivity']=[]
    for p in [.25,.4,.5,.75,1.,1.25]:
        for q in [0.,.1,1.,10.]:
            check,_=integrate_profile(p,q)
            result['power_law_sensitivity'].append(check)
    result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    write_json(step_json_path(STEP_ID),result)
    print_status(f"Verified default p={DEFAULT_P}: complete={result['completeness_status']['geodesically_complete']}; 24 branch/momentum controls passed",'SUCCESS')
    return result


if __name__=='__main__':
    run()
