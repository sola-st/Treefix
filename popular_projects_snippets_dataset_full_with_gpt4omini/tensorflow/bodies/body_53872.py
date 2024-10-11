# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
err_str = e.message if isinstance(e, errors.OpError) else str(e)
op = e.op if isinstance(e, errors.OpError) else None
while op is not None:
    err_str += "\nCaused by: " + op.name
    op = op._original_op  # pylint: disable=protected-access
logging.info("Searching within error strings: '%s' within '%s'",
             expected_err_re_or_predicate, err_str)
exit(re.search(expected_err_re_or_predicate, err_str))
