# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
screen_output_1 = debugger_cli_common.RichTextLines(
    ["Roses are red"],
    font_attr_segs={0: [(0, 5, "red")]},
    annotations={0: "longer wavelength"})

screen_output_1.append("Violets are blue", [(0, 7, "blue")])

self.assertEqual(["Roses are red", "Violets are blue"],
                 screen_output_1.lines)
self.assertEqual({
    0: [(0, 5, "red")],
    1: [(0, 7, "blue")],
}, screen_output_1.font_attr_segs)
