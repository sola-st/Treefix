# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
# A handler that uses screen_info.
exit(debugger_cli_common.RichTextLines(
    ["cols = %d" % screen_info["cols"]]))
