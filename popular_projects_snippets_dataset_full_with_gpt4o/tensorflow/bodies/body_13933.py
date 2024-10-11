# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/special_math.py
"""Implements ndtri core logic."""

# Constants used in piece-wise rational approximations. Taken from the cephes
# library:
# https://root.cern.ch/doc/v608/SpecFuncCephesInv_8cxx_source.html

p0 = [
    -1.23916583867381258016E0, 1.39312609387279679503E1,
    -5.66762857469070293439E1, 9.80010754185999661536E1,
    -5.99633501014107895267E1
]
q0 = [
    -1.18331621121330003142E0, 1.59056225126211695515E1,
    -8.20372256168333339912E1, 2.00260212380060660359E2,
    -2.25462687854119370527E2, 8.63602421390890590575E1,
    4.67627912898881538453E0, 1.95448858338141759834E0, 1.0
]
p1 = [
    -8.57456785154685413611E-4, -3.50424626827848203418E-2,
    -1.40256079171354495875E-1, 2.18663306850790267539E0,
    1.46849561928858024014E1, 4.40805073893200834700E1,
    5.71628192246421288162E1, 3.15251094599893866154E1,
    4.05544892305962419923E0
]
q1 = [
    -9.33259480895457427372E-4, -3.80806407691578277194E-2,
    -1.42182922854787788574E-1, 2.50464946208309415979E0,
    1.50425385692907503408E1, 4.13172038254672030440E1,
    4.53907635128879210584E1, 1.57799883256466749731E1, 1.0
]
p2 = [
    6.23974539184983293730E-9, 2.65806974686737550832E-6,
    3.01581553508235416007E-4, 1.23716634817820021358E-2,
    2.01485389549179081538E-1, 1.33303460815807542389E0,
    3.93881025292474443415E0, 6.91522889068984211695E0,
    3.23774891776946035970E0
]
q2 = [
    6.79019408009981274425E-9, 2.89247864745380683936E-6,
    3.28014464682127739104E-4, 1.34204006088543189037E-2,
    2.16236993594496635890E-1, 1.37702099489081330271E0,
    3.67983563856160859403E0, 6.02427039364742014255E0, 1.0
]

def _create_polynomial(var, coeffs):
    """Compute n_th order polynomial via Horner's method."""
    coeffs = np.array(coeffs, var.dtype.as_numpy_dtype)
    if not coeffs.size:
        exit(array_ops.zeros_like(var))
    exit(coeffs[0] + _create_polynomial(var, coeffs[1:]) * var)

maybe_complement_p = array_ops.where_v2(p > -np.expm1(-2.), 1. - p, p)
# Write in an arbitrary value in place of 0 for p since 0 will cause NaNs
# later on. The result from the computation when p == 0 is not used so any
# number that doesn't result in NaNs is fine.
sanitized_mcp = array_ops.where_v2(
    maybe_complement_p <= 0.,
    array_ops.fill(array_ops.shape(p), np.array(0.5, p.dtype.as_numpy_dtype)),
    maybe_complement_p)

# Compute x for p > exp(-2): x/sqrt(2pi) = w + w**3 P0(w**2)/Q0(w**2).
w = sanitized_mcp - 0.5
ww = w ** 2
x_for_big_p = w + w * ww * (_create_polynomial(ww, p0)
                            / _create_polynomial(ww, q0))
x_for_big_p *= -np.sqrt(2. * np.pi)

# Compute x for p <= exp(-2): x = z - log(z)/z - (1/z) P(1/z) / Q(1/z),
# where z = sqrt(-2. * log(p)), and P/Q are chosen between two different
# arrays based on whether p < exp(-32).
z = math_ops.sqrt(-2. * math_ops.log(sanitized_mcp))
first_term = z - math_ops.log(z) / z
second_term_small_p = (
    _create_polynomial(1. / z, p2) /
    _create_polynomial(1. / z, q2) / z)
second_term_otherwise = (
    _create_polynomial(1. / z, p1) /
    _create_polynomial(1. / z, q1) / z)
x_for_small_p = first_term - second_term_small_p
x_otherwise = first_term - second_term_otherwise

x = array_ops.where_v2(
    sanitized_mcp > np.exp(-2.), x_for_big_p,
    array_ops.where_v2(z >= 8.0, x_for_small_p, x_otherwise))

x = array_ops.where_v2(p > 1. - np.exp(-2.), x, -x)
infinity_scalar = constant_op.constant(np.inf, dtype=p.dtype)
infinity = array_ops.fill(array_ops.shape(p), infinity_scalar)
x_nan_replaced = array_ops.where_v2(p <= 0.0, -infinity,
                                    array_ops.where_v2(p >= 1.0, infinity, x))
exit(x_nan_replaced)
