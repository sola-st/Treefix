# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_test_util.py
"""Assert `bijector`'s forward/inverse/inverse_log_det_jacobian are congruent.

  We draw samples `X ~ U(lower_x, upper_x)`, then feed these through the
  `bijector` in order to check that:

  1. the forward is strictly monotonic.
  2. the forward/inverse methods are inverses of each other.
  3. the jacobian is the correct change of measure.

  This can only be used for a Bijector mapping open subsets of the real line
  to themselves.  This is due to the fact that this test compares the `prob`
  before/after transformation with the Lebesgue measure on the line.

  Args:
    bijector:  Instance of Bijector
    lower_x:  Python scalar.
    upper_x:  Python scalar.  Must have `lower_x < upper_x`, and both must be in
      the domain of the `bijector`.  The `bijector` should probably not produce
      huge variation in values in the interval `(lower_x, upper_x)`, or else
      the variance based check of the Jacobian will require small `rtol` or
      huge `n`.
    n:  Number of samples to draw for the checks.
    rtol:  Positive number.  Used for the Jacobian check.
    sess:  `tf.compat.v1.Session`.  Defaults to the default session.

  Raises:
    AssertionError:  If tests fail.
  """
# Checks and defaults.
if sess is None:
    sess = ops.get_default_session()

# Should be monotonic over this interval
ten_x_pts = np.linspace(lower_x, upper_x, num=10).astype(np.float32)
if bijector.dtype is not None:
    ten_x_pts = ten_x_pts.astype(bijector.dtype.as_numpy_dtype)
forward_on_10_pts = bijector.forward(ten_x_pts)

# Set the lower/upper limits in the range of the bijector.
lower_y, upper_y = sess.run(
    [bijector.forward(lower_x), bijector.forward(upper_x)])
if upper_y < lower_y:  # If bijector.forward is a decreasing function.
    lower_y, upper_y = upper_y, lower_y

# Uniform samples from the domain, range.
uniform_x_samps = uniform_lib.Uniform(
    low=lower_x, high=upper_x).sample(n, seed=0)
uniform_y_samps = uniform_lib.Uniform(
    low=lower_y, high=upper_y).sample(n, seed=1)

# These compositions should be the identity.
inverse_forward_x = bijector.inverse(bijector.forward(uniform_x_samps))
forward_inverse_y = bijector.forward(bijector.inverse(uniform_y_samps))

# For a < b, and transformation y = y(x),
# (b - a) = \int_a^b dx = \int_{y(a)}^{y(b)} |dx/dy| dy
# "change_measure_dy_dx" below is a Monte Carlo approximation to the right
# hand side, which should then be close to the left, which is (b - a).
# We assume event_ndims=0 because we assume scalar -> scalar. The log_det
# methods will handle whether they expect event_ndims > 0.
dy_dx = math_ops.exp(bijector.inverse_log_det_jacobian(
    uniform_y_samps, event_ndims=0))
# E[|dx/dy|] under Uniform[lower_y, upper_y]
# = \int_{y(a)}^{y(b)} |dx/dy| dP(u), where dP(u) is the uniform measure
expectation_of_dy_dx_under_uniform = math_ops.reduce_mean(dy_dx)
# dy = dP(u) * (upper_y - lower_y)
change_measure_dy_dx = (
    (upper_y - lower_y) * expectation_of_dy_dx_under_uniform)

# We'll also check that dy_dx = 1 / dx_dy.
dx_dy = math_ops.exp(
    bijector.forward_log_det_jacobian(
        bijector.inverse(uniform_y_samps), event_ndims=0))

[
    forward_on_10_pts_v,
    dy_dx_v,
    dx_dy_v,
    change_measure_dy_dx_v,
    uniform_x_samps_v,
    uniform_y_samps_v,
    inverse_forward_x_v,
    forward_inverse_y_v,
] = sess.run([
    forward_on_10_pts,
    dy_dx,
    dx_dy,
    change_measure_dy_dx,
    uniform_x_samps,
    uniform_y_samps,
    inverse_forward_x,
    forward_inverse_y,
])

assert_strictly_monotonic(forward_on_10_pts_v)
# Composition of forward/inverse should be the identity.
np.testing.assert_allclose(
    inverse_forward_x_v, uniform_x_samps_v, atol=1e-5, rtol=1e-3)
np.testing.assert_allclose(
    forward_inverse_y_v, uniform_y_samps_v, atol=1e-5, rtol=1e-3)
# Change of measure should be correct.
np.testing.assert_allclose(
    upper_x - lower_x, change_measure_dy_dx_v, atol=0, rtol=rtol)
# Inverse Jacobian should be equivalent to the reciprocal of the forward
# Jacobian.
np.testing.assert_allclose(
    dy_dx_v, np.divide(1., dx_dy_v), atol=1e-5, rtol=1e-3)
