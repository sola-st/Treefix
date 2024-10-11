# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_slice_test.py
"""Helper function for testing StructuredTensor.__getitem__.

    Checks that calling `struct.__getitem__(slice_spec) returns the expected
    value.  Checks three different configurations for each slice spec:

      * Call __getitem__ with the slice spec as-is (with int values)
      * Call __getitem__ with int values in the slice spec wrapped in
        `tf.constant()`.
      * Call __getitem__ with int values in the slice spec wrapped in
        `tf.compat.v1.placeholder()` (so value is not known at graph
        construction time).

    Args:
      struct: The StructuredTensor to test.
      slice_spec: The slice spec.
      expected: The expected value of struct.__getitem__(slice_spec), as a
        python list.
    """
tensor_slice_spec1 = _make_tensor_slice_spec(slice_spec, True)
tensor_slice_spec2 = _make_tensor_slice_spec(slice_spec, False)
value1 = struct.__getitem__(slice_spec)
value2 = struct.__getitem__(tensor_slice_spec1)
value3 = struct.__getitem__(tensor_slice_spec2)
self.assertAllEqual(value1, expected, "slice_spec=%s" % (slice_spec,))
self.assertAllEqual(value2, expected, "slice_spec=%s" % (slice_spec,))
self.assertAllEqual(value3, expected, "slice_spec=%s" % (slice_spec,))
