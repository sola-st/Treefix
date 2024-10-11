# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
a = np.linspace(0.0, 1.0 - 1.0 / 40.0, 40).reshape([2, 20])

out = tensor_format.format_tensor(
    a, "a", np_printoptions={"linewidth": 50})

self.assertEqual(
    {"dtype": a.dtype, "shape": a.shape},
    out.annotations["tensor_metadata"])

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["Tensor \"a\":", ""], out.lines[:2])
self.assertEqual(repr(a).split("\n"), out.lines[2:])

self._checkTensorMetadata(a, out.annotations)

# Check annotations for the beginning indices of the lines.
self._checkBeginIndicesAnnotations(out, a)
