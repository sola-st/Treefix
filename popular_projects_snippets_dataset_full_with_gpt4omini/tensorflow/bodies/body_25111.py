# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
a = np.linspace(0.0, 1.0 - 1.0 / 16.0, 16).reshape([4, 4])

out = tensor_format.format_tensor(a, "a", include_metadata=True)

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self,
    ["Tensor \"a\":",
     "  dtype: float64",
     "  shape: (4, 4)",
     ""], out.lines[:4])
self.assertEqual(repr(a).split("\n"), out.lines[4:])

self._checkTensorMetadata(a, out.annotations)
self._checkBeginIndicesAnnotations(out, a)
