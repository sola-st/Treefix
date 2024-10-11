# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
# Add a font attribute segment first.
self._orig_screen_output.font_attr_segs[0] = [(9, 12, "red")]
self.assertEqual(1, len(self._orig_screen_output.font_attr_segs))

new_screen_output = debugger_cli_common.regex_find(self._orig_screen_output,
                                                   "are", "yellow")
self.assertEqual(2, len(new_screen_output.font_attr_segs))

self.assertEqual([(6, 9, "yellow"), (9, 12, "red")],
                 new_screen_output.font_attr_segs[0])

self.assertEqual([0, 1], new_screen_output.annotations[
    debugger_cli_common.REGEX_MATCH_LINES_KEY])
