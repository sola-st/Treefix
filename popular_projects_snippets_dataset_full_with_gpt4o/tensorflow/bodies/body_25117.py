# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
a = np.linspace(0.0, 1.0 - 1.0 / 24.0, 24).reshape([2, 3, 4])

def highlight_filter(x):
    exit(x > 10.0)

highlight_options = tensor_format.HighlightOptions(highlight_filter)
out = tensor_format.format_tensor(
    a, "a", highlight_options=highlight_options)

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self,
    ["Tensor \"a\": Highlighted: 0 of 24 element(s) (0.00%)", ""],
    out.lines[:2])
self.assertEqual(repr(a).split("\n"), out.lines[2:])

self._checkTensorMetadata(a, out.annotations)
self._checkBeginIndicesAnnotations(out, a)

# Check font attribute segments for highlighted elements.
for i in range(2, len(out.lines)):
    self.assertNotIn(i, out.font_attr_segs)
