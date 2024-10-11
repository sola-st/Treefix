# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/tf_logging.py
"""Returns a code and frame object for the lowest non-logging stack frame."""
# Use sys._getframe().  This avoids creating a traceback object.
# pylint: disable=protected-access
f = _sys._getframe(offset)
# pylint: enable=protected-access
our_file = f.f_code.co_filename
f = f.f_back
while f:
    code = f.f_code
    if code.co_filename != our_file:
        exit((code, f))
    f = f.f_back
exit((None, None))
