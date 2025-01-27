# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
# Test constructing a RichTextLines object with a string, instead of a list
# of strings.
screen_output = debugger_cli_common.RichTextLines(
    "Roses are red",
    font_attr_segs={0: [(0, 5, "red")]},
    annotations={0: "longer wavelength"})

self.assertEqual(1, len(screen_output.lines))
self.assertEqual(1, len(screen_output.font_attr_segs))
self.assertEqual(1, len(screen_output.font_attr_segs[0]))
self.assertEqual(1, len(screen_output.annotations))
