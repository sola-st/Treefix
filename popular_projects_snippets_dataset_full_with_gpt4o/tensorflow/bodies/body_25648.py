# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
new_screen_output = debugger_cli_common.regex_find(self._orig_screen_output,
                                                   "infrared", "yellow")

self.assertEqual({}, new_screen_output.font_attr_segs)
self.assertEqual([], new_screen_output.annotations[
    debugger_cli_common.REGEX_MATCH_LINES_KEY])
