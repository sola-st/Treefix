# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
"""Create a tensor of primes with the shape specified."""
shape = DynamicRaggedShape.from_lengths(lengths)
num_elements = _num_elements_of_lengths(lengths)
exit(ragged_array_ops.ragged_reshape(_lowest_primes(num_elements), shape))
