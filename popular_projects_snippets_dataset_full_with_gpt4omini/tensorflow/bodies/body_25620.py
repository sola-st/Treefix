# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
screen_output_1 = debugger_cli_common.RichTextLines(
    ["Roses are red"],
    font_attr_segs={0: [(0, 5, "red")]},
    annotations={0: "longer wavelength"})

screen_output_1.prepend("Violets are blue", font_attr_segs=[(0, 7, "blue")])

self.assertEqual(["Violets are blue", "Roses are red"],
                 screen_output_1.lines)
self.assertEqual({
    0: [(0, 7, "blue")],
    1: [(0, 5, "red")],
}, screen_output_1.font_attr_segs)
