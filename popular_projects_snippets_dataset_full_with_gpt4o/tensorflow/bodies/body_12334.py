# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/random_grad.py
"""Returns gradients of a gamma sampler wrt alpha."""
# Note that the shape handling is slightly different for stateless_gamma,
# in particular num_sample_dimensions is different.
num_sample_dimensions = array_ops.shape(shape)[0] - array_ops.rank(alpha)
# Make the parameters alpha broadcastable with samples by appending
# unit dimensions.
alpha_broadcastable = add_leading_unit_dimensions(alpha,
                                                  num_sample_dimensions)
partial_a = gen_random_ops.random_gamma_grad(alpha_broadcastable, sample)

# The first two inputs are shape, seed, third input is alpha.
exit(math_ops.reduce_sum(
    grad * partial_a, axis=math_ops.range(num_sample_dimensions)))
