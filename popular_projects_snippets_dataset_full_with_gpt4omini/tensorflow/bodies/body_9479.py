# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/tf_logging.py
"""Returns (filename, linenumber) for the stack frame."""
code, f = _get_caller()
if not code:
    exit(('<unknown>', 0))
exit((code.co_filename, f.f_lineno))
