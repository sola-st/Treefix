# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
"""Tests that ragged_to_dense generates the right gradient.

    Args:
      shape: The `shape` arg for `ragged_to_dense`.
      rt_value: The `rt_input` arg for `ragged_to_dense`.
      rt_grad: The expected gradient for `rt_value`.  Corresponds 1:1 with
        `rt_value`.
      default_value: The `default_value` arg for `ragged_to_dense`.
      default_grad: The expected gradient for `default_value`.  Corresponds 1:1
        with `default_value`.
      output_value: The expected output of `ragged_to_dense`.
      output_grad: The gradient for the output (used to generate the gradients
        `rt_grad` and `default_grad`).  Corresponds 1:1 with `output_value`.
      ragged_rank: Ragged rank for `rt_value`.
    """
rt_value = ragged_factory_ops.constant(
    rt_value, dtype=dtypes.float32, ragged_rank=ragged_rank)
rt_grad = ragged_factory_ops.constant(
    rt_grad, dtype=dtypes.float32, ragged_rank=ragged_rank)
default_value = constant_op.constant(default_value, dtype=dtypes.float32)
default_grad = constant_op.constant(default_grad, dtype=dtypes.float32)
output_value = constant_op.constant(
    output_value, dtype=dtypes.float32, shape=shape)
output_grad = constant_op.constant(
    output_grad, dtype=dtypes.float32, shape=shape)
shape = tensor_shape.as_shape(shape)

# There are different code paths for ragged_to_dense, depending on whether
# the RaggedTensor was created from row_splits or value_rowids.  Make sure
# that we test both.
for partition_type in ['row_splits', 'value_rowids']:
    rt_val = self.rt_with_partition_type(rt_value, partition_type)
    if context.executing_eagerly():
        self._test_gradient_helper(rt_val, default_value, shape, output_grad,
                                   output_value, rt_grad, default_grad)
    else:
        # There are different code paths when computing the gradient for
        # default_value, depending on whether shape info is statically
        # available; make sure that we test all code paths.
        for shape_info in ['known', 'unknown_dims', 'unknown_rank']:
            rt_val = self.wrap_in_placeholder(rt_val, shape_info)
            default_val = self.wrap_in_placeholder(default_value, shape_info)
            shape_val = self.wrap_in_placeholder(shape, shape_info)
            self._test_gradient_helper(rt_val, default_val, shape_val,
                                       output_grad, output_value, rt_grad,
                                       default_grad)
