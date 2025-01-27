# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
screen_output = debugger_cli_common.RichTextLines(
    ["Roses are red", "Violets are blue"])

self.assertEqual(2, len(screen_output.lines))

screen_output.lines.append("Sugar is sweet")
self.assertEqual(3, len(screen_output.lines))
