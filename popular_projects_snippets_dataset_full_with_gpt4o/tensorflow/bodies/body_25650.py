# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
rich_lines = debugger_cli_common.RichTextLines(["Violets are blue"])
rich_lines.prepend(["Roses are red"])
searched_rich_lines = debugger_cli_common.regex_find(
    rich_lines, "red", "bold")
self.assertEqual(
    {0: [(10, 13, "bold")]}, searched_rich_lines.font_attr_segs)

rich_lines = debugger_cli_common.RichTextLines(["Violets are blue"])
rich_lines.prepend(["A poem"], font_attr_segs=[(0, 1, "underline")])
searched_rich_lines = debugger_cli_common.regex_find(
    rich_lines, "poem", "italic")
self.assertEqual(
    {0: [(0, 1, "underline"), (2, 6, "italic")]},
    searched_rich_lines.font_attr_segs)
