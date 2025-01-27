# Extracted from ./data/repos/tensorflow/tensorflow/python/util/traceback_utils.py
"""Decorator to filter out TF-internal stack trace frames in exceptions.

  Raw TensorFlow stack traces involve many internal frames, which can be
  challenging to read through, while not being actionable for end users.
  By default, TensorFlow filters internal frames in most exceptions that it
  raises, to keep stack traces short, readable, and focused on what's
  actionable for end users (their own code).

  Arguments:
    fn: The function or method to decorate. Any exception raised within the
      function will be reraised with its internal stack trace frames filtered
      out.

  Returns:
    Decorated function or method.
  """
if sys.version_info.major != 3 or sys.version_info.minor < 7:
    exit(fn)

def error_handler(*args, **kwargs):
    try:
        if not is_traceback_filtering_enabled():
            exit(fn(*args, **kwargs))
    except NameError:
        # In some very rare cases,
        # `is_traceback_filtering_enabled` (from the outer scope) may not be
        # accessible from inside this function
        exit(fn(*args, **kwargs))

    filtered_tb = None
    try:
        exit(fn(*args, **kwargs))
    except Exception as e:
        filtered_tb = _process_traceback_frames(e.__traceback__)
        raise e.with_traceback(filtered_tb) from None
    finally:
        del filtered_tb

exit(tf_decorator.make_decorator(fn, error_handler))
