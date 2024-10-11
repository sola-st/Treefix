# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem_test.py
"""Helper function for testing RaggedTensor.__getitem__ exceptions."""
tensor_slice_spec = _make_tensor_slice_spec(slice_spec, True)
with self.assertRaisesRegex(expected, message):
    self.evaluate(rt.__getitem__(slice_spec))
with self.assertRaisesRegex(expected, message):
    self.evaluate(rt.__getitem__(tensor_slice_spec))
