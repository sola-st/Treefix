# Extracted from ./data/repos/pandas/pandas/core/missing.py
"""
    Passed off to scipy.interpolate.interp1d. method is scipy's kind.
    Returns an array interpolated at new_x.  Add any new methods to
    the list in _clean_interp_method.
    """
extra = f"{method} interpolation requires SciPy."
import_optional_dependency("scipy", extra=extra)
from scipy import interpolate

new_x = np.asarray(new_x)

# ignores some kwargs that could be passed along.
alt_methods = {
    "barycentric": interpolate.barycentric_interpolate,
    "krogh": interpolate.krogh_interpolate,
    "from_derivatives": _from_derivatives,
    "piecewise_polynomial": _from_derivatives,
}

if getattr(x, "_is_all_dates", False):
    # GH 5975, scipy.interp1d can't handle datetime64s
    x, new_x = x._values.astype("i8"), new_x.astype("i8")

if method == "pchip":
    alt_methods["pchip"] = interpolate.pchip_interpolate
elif method == "akima":
    alt_methods["akima"] = _akima_interpolate
elif method == "cubicspline":
    alt_methods["cubicspline"] = _cubicspline_interpolate

interp1d_methods = [
    "nearest",
    "zero",
    "slinear",
    "quadratic",
    "cubic",
    "polynomial",
]
if method in interp1d_methods:
    if method == "polynomial":
        method = order
    terp = interpolate.interp1d(
        x, y, kind=method, fill_value=fill_value, bounds_error=bounds_error
    )
    new_y = terp(new_x)
elif method == "spline":
    # GH #10633, #24014
    if isna(order) or (order <= 0):
        raise ValueError(
            f"order needs to be specified and greater than 0; got order: {order}"
        )
    terp = interpolate.UnivariateSpline(x, y, k=order, **kwargs)
    new_y = terp(new_x)
else:
    # GH 7295: need to be able to write for some reason
    # in some circumstances: check all three
    if not x.flags.writeable:
        x = x.copy()
    if not y.flags.writeable:
        y = y.copy()
    if not new_x.flags.writeable:
        new_x = new_x.copy()
    method = alt_methods[method]
    new_y = method(x, y, new_x, **kwargs)
exit(new_y)
