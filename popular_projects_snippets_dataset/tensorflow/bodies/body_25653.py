# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
out, new_line_indices = debugger_cli_common.wrap_rich_text_lines(
    self._orig_screen_output, 11)

# Add non-row-index field to out.
out.annotations["metadata"] = "foo"

# Check wrapped text.
self.assertEqual(5, len(out.lines))
self.assertEqual("Folk song:", out.lines[0])
self.assertEqual("Roses are r", out.lines[1])
self.assertEqual("ed", out.lines[2])
self.assertEqual("Violets are", out.lines[3])
self.assertEqual(" blue", out.lines[4])

# Check wrapped font_attr_segs.
self.assertFalse(0 in out.font_attr_segs)
self.assertEqual([(0, 5, "red"), (6, 9, "gray"), (10, 11, "red")],
                 out.font_attr_segs[1])
self.assertEqual([(0, 1, "red"), (1, 2, "crimson")], out.font_attr_segs[2])
self.assertEqual([(0, 7, "blue"), (8, 11, "gray")], out.font_attr_segs[3])
self.assertEqual([(1, 3, "blue"), (3, 5, "indigo")], out.font_attr_segs[4])

# Check annotations.
self.assertFalse(0 in out.annotations)
self.assertEqual("longer wavelength", out.annotations[1])
self.assertFalse(2 in out.annotations)
self.assertEqual("shorter wavelength", out.annotations[3])
self.assertFalse(4 in out.annotations)

# Chec that the non-row-index field is present in output.
self.assertEqual("foo", out.annotations["metadata"])

self.assertEqual(new_line_indices, [0, 1, 3])
