# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
with self.assertRaisesRegex(ValueError,
                            "Invalid type of input screen_output"):
    debugger_cli_common.wrap_rich_text_lines("foo", 12)

with self.assertRaisesRegex(ValueError, "Invalid type of input cols"):
    debugger_cli_common.wrap_rich_text_lines(
        debugger_cli_common.RichTextLines(["foo", "bar"]), "12")
