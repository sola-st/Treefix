# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
a = np.array(42, dtype=np.int32)

out = tensor_format.format_tensor(a, "a")

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["Tensor \"a\":", ""], out.lines[:2])
self.assertTrue(out.lines[2].startswith("array(42"))
self._checkTensorMetadata(a, out.annotations)
