# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
out, new_line_indices = debugger_cli_common.wrap_rich_text_lines(
    debugger_cli_common.RichTextLines([]), 10)

self.assertEqual([], out.lines)
self.assertEqual([], new_line_indices)
