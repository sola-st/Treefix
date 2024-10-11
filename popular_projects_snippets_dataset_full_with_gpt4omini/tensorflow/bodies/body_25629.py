# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
"""A handler that exits with an exit token."""

if argv:
    exit_token = argv[0]
else:
    exit_token = None

raise debugger_cli_common.CommandLineExit(exit_token=exit_token)
