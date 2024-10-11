# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
r"""Computes \\(ln(|Beta(x)|)\\), reducing along the last dimension.

  Given one-dimensional $z = [z_1,...,z_K]$, we define

  $$Beta(z) = \frac{\prod_j \Gamma(z_j)}{\Gamma(\sum_j z_j)},$$

  where $\Gamma$ is the gamma function.

  And for $n + 1$ dimensional $x$ with shape $[N_1, ..., N_n, K]$, we define

  $$lbeta(x)[i_1, ..., i_n] = \log{|Beta(x[i_1, ..., i_n, :])|}.$$

  In other words, the last dimension is treated as the $z$ vector.

  Note that if $z = [u, v]$, then

  $$Beta(z) = \frac{\Gamma(u)\Gamma(v)}{\Gamma(u + v)}
    = \int_0^1 t^{u-1} (1 - t)^{v-1} \mathrm{d}t,$$

  which defines the traditional bivariate beta function.

  If the last dimension is empty, we follow the convention that the sum over
  the empty set is zero, and the product is one.

  Args:
    x: A rank `n + 1` `Tensor`, `n >= 0` with type `float`, or `double`.
    name: A name for the operation (optional).

  Returns:
    The logarithm of \\(|Beta(x)|\\) reducing along the last dimension.
  """
# In the event that the last dimension has zero entries, we return -inf.
# This is consistent with a convention that the sum over the empty set 0, and
# the product is 1.
# This is standard.  See https://en.wikipedia.org/wiki/Empty_set.
with ops.name_scope(name, 'lbeta', [x]):
    x = ops.convert_to_tensor(x, name='x')

    # Note reduce_sum([]) = 0.
    log_prod_gamma_x = math_ops.reduce_sum(math_ops.lgamma(x), axis=[-1])

    # Note lgamma(0) = infinity, so if x = []
    # log_gamma_sum_x = lgamma(0) = infinity, and
    # log_prod_gamma_x = lgamma(1) = 0,
    # so result = -infinity
    sum_x = math_ops.reduce_sum(x, axis=[-1])
    log_gamma_sum_x = math_ops.lgamma(sum_x)
    result = log_prod_gamma_x - log_gamma_sum_x

    exit(result)
