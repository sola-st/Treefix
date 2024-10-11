# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
rtl = debugger_cli_common.RichTextLines(
    "Roses are red",
    font_attr_segs={0: [(0, 5, "red")]})
rtl.append_rich_line(debugger_cli_common.RichLine("Violets are ") +
                     debugger_cli_common.RichLine("blue", "blue"))
self.assertEqual(2, len(rtl.lines))
self.assertEqual(2, len(rtl.font_attr_segs))
self.assertEqual(1, len(rtl.font_attr_segs[0]))
self.assertEqual(1, len(rtl.font_attr_segs[1]))
