# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Testing the shape has enough information.
# In particular, any uniform_row_length should be reproduced.
if context.executing_eagerly():
    exit()
shape = DynamicRaggedShape.from_lengths(
    lengths, num_row_partitions=num_row_partitions)
rt_a = ragged_array_ops.ragged_reshape(
    _lowest_primes(_num_elements_of_lengths(lengths)), shape)
shape_e = tensor_shape.TensorShape(shape_e)
self.assertEqual(shape_e.as_list(), rt_a.shape.as_list())
