# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
a = np.zeros(20)

out = tensor_format.format_tensor(
    a, "a", np_printoptions={"linewidth": 40})

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["Tensor \"a\":", ""], out.lines[:2])
self.assertEqual(repr(a).split("\n"), out.lines[2:])

self._checkTensorElementLocations(out, a)
