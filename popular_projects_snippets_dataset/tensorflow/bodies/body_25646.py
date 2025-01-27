# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
new_screen_output = debugger_cli_common.regex_find(self._orig_screen_output,
                                                   "are", "yellow")

self.assertEqual(2, len(new_screen_output.font_attr_segs))
self.assertEqual([(6, 9, "yellow")], new_screen_output.font_attr_segs[0])
self.assertEqual([(8, 11, "yellow")], new_screen_output.font_attr_segs[1])

# Check field in annotations carrying a list of matching line indices.
self.assertEqual([0, 1], new_screen_output.annotations[
    debugger_cli_common.REGEX_MATCH_LINES_KEY])
