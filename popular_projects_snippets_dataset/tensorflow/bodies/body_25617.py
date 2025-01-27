# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
screen_output_1 = debugger_cli_common.RichTextLines(
    ["Roses are red", "Violets are blue"],
    font_attr_segs={0: [(0, 5, "red")],
                    1: [(0, 7, "blue")]},
    annotations={0: "longer wavelength",
                 1: "shorter wavelength"})
screen_output_2 = debugger_cli_common.RichTextLines([])

screen_output_1.extend(screen_output_2)

self.assertEqual(2, screen_output_1.num_lines())
self.assertEqual(["Roses are red", "Violets are blue"],
                 screen_output_1.lines)
self.assertEqual({
    0: [(0, 5, "red")],
    1: [(0, 7, "blue")],
}, screen_output_1.font_attr_segs)
self.assertEqual({
    0: [(0, 5, "red")],
    1: [(0, 7, "blue")],
}, screen_output_1.font_attr_segs)
self.assertEqual({
    0: "longer wavelength",
    1: "shorter wavelength",
}, screen_output_1.annotations)
