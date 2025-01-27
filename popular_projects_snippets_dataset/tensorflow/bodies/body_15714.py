# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem_test.py
"""Helper function for testing RaggedTensor.__getitem__.

    Checks that calling `rt.__getitem__(slice_spec) returns the expected value.
    Checks three different configurations for each slice spec:

      * Call __getitem__ with the slice spec as-is (with int values)
      * Call __getitem__ with int values in the slice spec wrapped in
        `tf.constant()`.
      * Call __getitem__ with int values in the slice spec wrapped in
        `tf.compat.v1.placeholder()` (so value is not known at graph
        construction time).

    Args:
      rt: The RaggedTensor to test.
      slice_spec: The slice spec.
      expected: The expected value of rt.__getitem__(slice_spec), as a python
        list; or an exception class.
      expected_shape: The expected shape for `rt.__getitem__(slice_spec)`.
    """
tensor_slice_spec1 = _make_tensor_slice_spec(slice_spec, True)
tensor_slice_spec2 = _make_tensor_slice_spec(slice_spec, False)
value1 = rt.__getitem__(slice_spec)
value2 = rt.__getitem__(tensor_slice_spec1)
value3 = rt.__getitem__(tensor_slice_spec2)
self.assertAllEqual(value1, expected, 'slice_spec=%s' % (slice_spec,))
self.assertAllEqual(value2, expected, 'slice_spec=%s' % (slice_spec,))
self.assertAllEqual(value3, expected, 'slice_spec=%s' % (slice_spec,))
if expected_shape is not None:
    value1.shape.assert_is_compatible_with(expected_shape)
    value2.shape.assert_is_compatible_with(expected_shape)
    value3.shape.assert_is_compatible_with(expected_shape)
