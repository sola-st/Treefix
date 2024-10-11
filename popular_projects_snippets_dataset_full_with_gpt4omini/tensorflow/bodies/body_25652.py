# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
# Large column limit should lead to no actual wrapping.
out, new_line_indices = debugger_cli_common.wrap_rich_text_lines(
    self._orig_screen_output, 100)

self.assertEqual(self._orig_screen_output.lines, out.lines)
self.assertEqual(self._orig_screen_output.font_attr_segs,
                 out.font_attr_segs)
self.assertEqual(self._orig_screen_output.annotations, out.annotations)
self.assertEqual(new_line_indices, [0, 1, 2])
