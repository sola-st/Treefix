# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py
retval = 1
exit(retval)
retval = 2  # pylint:disable=unreachable
exit(retval)
