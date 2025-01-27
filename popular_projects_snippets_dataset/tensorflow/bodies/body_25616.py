# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
screen_output_1 = debugger_cli_common.RichTextLines(
    ["Roses are red", "Violets are blue"],
    font_attr_segs={0: [(0, 5, "red")],
                    1: [(0, 7, "blue")]},
    annotations={0: "longer wavelength",
                 1: "shorter wavelength"})
screen_output_2 = debugger_cli_common.RichTextLines(
    ["Lilies are white", "Sunflowers are yellow"],
    font_attr_segs={0: [(0, 6, "white")],
                    1: [(0, 7, "yellow")]},
    annotations={
        "metadata": "foo",
        0: "full spectrum",
        1: "medium wavelength"
    })

screen_output_1.extend(screen_output_2)

self.assertEqual(4, screen_output_1.num_lines())
self.assertEqual([
    "Roses are red", "Violets are blue", "Lilies are white",
    "Sunflowers are yellow"
], screen_output_1.lines)
self.assertEqual({
    0: [(0, 5, "red")],
    1: [(0, 7, "blue")],
    2: [(0, 6, "white")],
    3: [(0, 7, "yellow")]
}, screen_output_1.font_attr_segs)
self.assertEqual({
    0: [(0, 5, "red")],
    1: [(0, 7, "blue")],
    2: [(0, 6, "white")],
    3: [(0, 7, "yellow")]
}, screen_output_1.font_attr_segs)
self.assertEqual({
    "metadata": "foo",
    0: "longer wavelength",
    1: "shorter wavelength",
    2: "full spectrum",
    3: "medium wavelength"
}, screen_output_1.annotations)
