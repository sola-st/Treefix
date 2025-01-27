# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""Check RichTextLines output for valid command prefix but invalid syntax."""

tst.assertEqual([
    "Syntax error for command: %s" % command_prefix,
    "For help, do \"help %s\"" % command_prefix
], out.lines)
