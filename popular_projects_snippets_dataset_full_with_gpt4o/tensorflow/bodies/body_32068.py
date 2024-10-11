# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
"""Tests reduce_join for one input and multiple axes.

    Does so by comparing the output to that from nested reduce_string_joins.
    The correctness of single-dimension reduce_join is verified by other
    tests below using _testReduceJoin.

    Args:
      input_array: The input to test.
      axis: The indices to reduce.
      separator: The separator to use when joining.
    """
with self.cached_session():
    output = string_ops.reduce_join(
        inputs=input_array, axis=axis, keep_dims=False, separator=separator)
    output_keep_dims = string_ops.reduce_join(
        inputs=input_array, axis=axis, keep_dims=True, separator=separator)

    truth = input_array
    for index in axis:
        truth = string_ops.reduce_join(
            inputs=truth, axis=index, keep_dims=True, separator=separator)
    if not axis:
        truth = constant_op.constant(truth)
    truth_squeezed = array_ops.squeeze(truth, axis=axis)
    output_array = self.evaluate(output)
    output_keep_dims_array = self.evaluate(output_keep_dims)
    truth_array = self.evaluate(truth)
    truth_squeezed_array = self.evaluate(truth_squeezed)
self.assertAllEqualUnicode(truth_array, output_keep_dims_array)
self.assertAllEqualUnicode(truth_squeezed_array, output_array)
self.assertAllEqual(truth.get_shape(), output_keep_dims.get_shape())
self.assertAllEqual(truth_squeezed.get_shape(), output.get_shape())
