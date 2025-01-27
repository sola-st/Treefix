# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self._orig_screen_output = debugger_cli_common.RichTextLines(
    ["Folk song:", "Roses are red", "Violets are blue"],
    font_attr_segs={1: [(0, 12, "red")],
                    2: [(1, 16, "blue")]},
    annotations={1: "longer wavelength",
                 2: "shorter wavelength"})

out, new_line_indices = debugger_cli_common.wrap_rich_text_lines(
    self._orig_screen_output, 5)

# Check wrapped text.
self.assertEqual(9, len(out.lines))
self.assertEqual("Folk ", out.lines[0])
self.assertEqual("song:", out.lines[1])
self.assertEqual("Roses", out.lines[2])
self.assertEqual(" are ", out.lines[3])
self.assertEqual("red", out.lines[4])
self.assertEqual("Viole", out.lines[5])
self.assertEqual("ts ar", out.lines[6])
self.assertEqual("e blu", out.lines[7])
self.assertEqual("e", out.lines[8])

# Check wrapped font_attr_segs.
self.assertFalse(0 in out.font_attr_segs)
self.assertFalse(1 in out.font_attr_segs)
self.assertEqual([(0, 5, "red")], out.font_attr_segs[2])
self.assertEqual([(0, 5, "red")], out.font_attr_segs[3])
self.assertEqual([(0, 2, "red")], out.font_attr_segs[4])
self.assertEqual([(1, 5, "blue")], out.font_attr_segs[5])
self.assertEqual([(0, 5, "blue")], out.font_attr_segs[6])
self.assertEqual([(0, 5, "blue")], out.font_attr_segs[7])
self.assertEqual([(0, 1, "blue")], out.font_attr_segs[8])

# Check annotations.
self.assertFalse(0 in out.annotations)
self.assertFalse(1 in out.annotations)
self.assertEqual("longer wavelength", out.annotations[2])
self.assertFalse(3 in out.annotations)
self.assertFalse(4 in out.annotations)
self.assertEqual("shorter wavelength", out.annotations[5])
self.assertFalse(6 in out.annotations)
self.assertFalse(7 in out.annotations)
self.assertFalse(8 in out.annotations)

self.assertEqual(new_line_indices, [0, 2, 5])
