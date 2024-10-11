# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
a = np.zeros(20)

out = tensor_format.format_tensor(
    a, "a", np_printoptions={"linewidth": 40})

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["Tensor \"a\":", ""], out.lines[:2])
self.assertEqual(repr(a).split("\n"), out.lines[2:])

self._checkTensorElementLocations(out, a)

with self.assertRaisesRegex(ValueError, "Indices exceed tensor dimensions"):
    tensor_format.locate_tensor_element(out, [20])

with self.assertRaisesRegex(ValueError, "Indices contain negative"):
    tensor_format.locate_tensor_element(out, [-1])

with self.assertRaisesRegex(ValueError, "Dimensions mismatch"):
    tensor_format.locate_tensor_element(out, [0, 0])
