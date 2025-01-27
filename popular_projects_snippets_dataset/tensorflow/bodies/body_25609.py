# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
# Test RichTextLines constructor.
screen_output = debugger_cli_common.RichTextLines(
    ["Roses are red", "Violets are blue"],
    font_attr_segs={0: [(0, 5, "red")],
                    1: [(0, 7, "blue")]},
    annotations={0: "longer wavelength",
                 1: "shorter wavelength"})

self.assertEqual(2, len(screen_output.lines))
self.assertEqual(2, len(screen_output.font_attr_segs))
self.assertEqual(1, len(screen_output.font_attr_segs[0]))
self.assertEqual(1, len(screen_output.font_attr_segs[1]))
self.assertEqual(2, len(screen_output.annotations))

self.assertEqual(2, screen_output.num_lines())
