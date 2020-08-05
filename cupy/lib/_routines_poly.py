import functools

import cupy


def _wraps_polyroutine(func):
    def _get_coeffs(x):
        if isinstance(x, cupy.poly1d):
            return x._coeffs
        if isinstance(x, cupy.ndarray) or cupy.isscalar(x):
            return cupy.atleast_1d(x)
        raise TypeError('Unsupported type')

    def wrapper(*args):
        coeffs = [_get_coeffs(x) for x in args]
        out = func(*coeffs)

        if all([not isinstance(x, cupy.poly1d) for x in args]):
            return out
        if isinstance(out, cupy.ndarray):
            return cupy.poly1d(out)
        if isinstance(out, tuple):
            return tuple([cupy.poly1d(x) for x in out])
        assert False  # Never reach

    return functools.update_wrapper(wrapper, func)


@_wraps_polyroutine
def polyadd(a1, a2):
    """Computes the sum of two polynomials.

    Args:
        a1 (scalar, cupy.ndarray or cupy.poly1d): first input polynomial.
        a2 (scalar, cupy.ndarray or cupy.poly1d): second input polynomial.

    Returns:
        cupy.ndarray or cupy.poly1d: The sum of the inputs.

    .. seealso:: :func:`numpy.polyadd`

    """
    if a1.size < a2.size:
        a1, a2 = a2, a1
    out = cupy.pad(a2, (a1.size - a2.size, 0))
    out = out.astype(cupy.result_type(a1, a2), copy=False)
    out += a1
    return out


@_wraps_polyroutine
def polysub(a1, a2):
    """Computes the difference of two polynomials.

    Args:
        a1 (scalar, cupy.ndarray or cupy.poly1d): first input polynomial.
        a2 (scalar, cupy.ndarray or cupy.poly1d): second input polynomial.

    Returns:
        cupy.ndarray or cupy.poly1d: The difference of the inputs.

    .. seealso:: :func:`numpy.polysub`

    """
    if a1.shape[0] <= a2.shape[0]:
        out = cupy.pad(a1, (a2.shape[0] - a1.shape[0], 0))
        out = out.astype(cupy.result_type(a1, a2), copy=False)
        out -= a2
    else:
        out = cupy.pad(a2, (a1.shape[0] - a2.shape[0], 0))
        out = out.astype(cupy.result_type(a1, a2), copy=False)
        out -= 2 * out - a1
    return out


def polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False):
    """Returns the least squares fit of polynomial of degree deg
    to the data y sampled at x.

    Args:
        x (cupy.ndarray): x-coordinates of the sample points of shape (M, ).
        y (cupy.ndarray): y-coordinates of the sample points of shape
            (M, ) or (M, K).
        deg (int): degree of the fitting polynomial.
        rcond (float, optional): relative condition number of the fit.
            The default value is len(x) * eps.
        full (bool, optional): indicator of the return value nature.
            When False (default), only the coefficients are returned.
            When True, diagnostic information is also returned.
        w (cupy.ndarray, optional): weights applied to the y-coordinates
            of the sample points of shape (M, ).
        cov (bool or str, optional): if given, returns tthe estimate with
            its covariance matrix.

    Returns:
        cupy.ndarray: of shape (deg + 1,) or (deg + 1, K)
            polynomial coefficients from highest to lowest degree.
        tuple (cupy.ndarray, int, cupy.ndarray, float): present if `full`=True
            sum of squared residuals of the least-squares fit,
            rank of the scaled Vandermonde coefficient matrix,
            its singular values, and the specified value of `rcond`.
        cupy.ndarray: of shape (M, M) or (M, M, K).
            Present only if `full` = False and `cov`=True
            The covariance matrix of the polynomial coefficient estimates.

    .. warning::

        numpy.RankWarning: The rank of the coefficient matrix in the
        least-squares fit is deficient. It is raised if `full`=False.

    .. seealso:: :func:`numpy.polyfit`

    """
    