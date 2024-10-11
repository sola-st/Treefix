# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
with self.assertRaisesRegex(ValueError, "Unexpected type in lines"):
    debugger_cli_common.RichTextLines(123)
