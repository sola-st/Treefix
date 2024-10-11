# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Returns a context manager to enclose code expected to raise an exception.

    If the exception is an OpError, the op stack is also included in the message
    predicate search.

    Args:
      exception_type: The expected type of exception that should be raised.
      expected_err_re_or_predicate: If this is callable, it should be a function
        of one argument that inspects the passed-in exception and returns True
        (success) or False (please fail the test). Otherwise, the error message
        is expected to match this regular expression partially.

    Returns:
      A context manager to surround code that is expected to raise an
      exception.
    """
if callable(expected_err_re_or_predicate):
    predicate = expected_err_re_or_predicate
else:

    def predicate(e):
        err_str = e.message if isinstance(e, errors.OpError) else str(e)
        op = e.op if isinstance(e, errors.OpError) else None
        while op is not None:
            err_str += "\nCaused by: " + op.name
            op = op._original_op  # pylint: disable=protected-access
        logging.info("Searching within error strings: '%s' within '%s'",
                     expected_err_re_or_predicate, err_str)
        exit(re.search(expected_err_re_or_predicate, err_str))

try:
    exit()
    self.fail(exception_type.__name__ + " not raised")
except Exception as e:  # pylint: disable=broad-except
    if not isinstance(e, exception_type) or not predicate(e):
        raise AssertionError("Exception of type %s: %s" %
                             (str(type(e)), str(e)))
