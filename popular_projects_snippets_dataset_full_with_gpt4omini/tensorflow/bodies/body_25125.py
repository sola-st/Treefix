# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
a = np.linspace(0.0, 1.0 - 1.0 / 16.0, 16).reshape([4, 4])

out = tensor_format.format_tensor(a, "a")

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["Tensor \"a\":", ""], out.lines[:2])
self.assertEqual(repr(a).split("\n"), out.lines[2:])

self._checkTensorElementLocations(out, a)

with self.assertRaisesRegex(ValueError, "Indices exceed tensor dimensions"):
    tensor_format.locate_tensor_element(out, [1, 4])

with self.assertRaisesRegex(ValueError, "Indices contain negative"):
    tensor_format.locate_tensor_element(out, [-1, 2])

with self.assertRaisesRegex(ValueError, "Dimensions mismatch"):
    tensor_format.locate_tensor_element(out, [0])
