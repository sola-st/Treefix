# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
"""Compares the output of reduce_join to an expected result.

    Args:
      input_array: The string input to be joined.
      truth: An array or np.array of the expected result.
      truth_shape: An array or np.array of the expected shape.
      axis: The indices to reduce over.
      keep_dims: Whether or not to retain reduced dimensions.
      separator: The separator to use for joining.
    """
with self.cached_session():
    output = string_ops.reduce_join(
        inputs=input_array,
        axis=axis,
        keep_dims=keep_dims,
        separator=separator)
    output_array = self.evaluate(output)

self.assertAllEqualUnicode(truth, output_array)
self.assertAllEqual(truth_shape, output.get_shape())
