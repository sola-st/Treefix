# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
if self._run_start_response == debugger_cli_common.EXPLICIT_USER_EXIT:
    # Explicit user "exit" command leads to sys.exit(1).
    print(
        "Note: user exited from debugger CLI: Calling sys.exit(1).",
        file=sys.stderr)
    sys.exit(1)
