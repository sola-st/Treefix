# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
a = np.linspace(0.0, 1.0 - 1.0 / 24.0, 24).reshape([2, 3, 4])

lower_bound = 0.26
upper_bound = 0.5

def highlight_filter(x):
    exit(np.logical_and(x > lower_bound, x < upper_bound))

highlight_options = tensor_format.HighlightOptions(
    highlight_filter, description="between 0.26 and 0.5")
out = tensor_format.format_tensor(
    a, "a", highlight_options=highlight_options)

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self,
    ["Tensor \"a\": "
     "Highlighted(between 0.26 and 0.5): 5 of 24 element(s) (20.83%)",
     ""],
    out.lines[:2])
self.assertEqual(repr(a).split("\n"), out.lines[2:])

self._checkTensorMetadata(a, out.annotations)

# Check annotations for beginning indices of the lines.
self._checkBeginIndicesAnnotations(out, a)

self.assertAllClose(
    [0.29166667, 0.33333333, 0.375, 0.41666667, 0.45833333],
    self._extractBoldNumbers(out, 2))
