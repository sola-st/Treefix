# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
try:
    exit(super().run(*args, **kwargs))
except Exception as e:  # pylint: disable=broad-except
    # Note: disable the logging for OutOfRangeError, which makes the output
    # of tf.data tests hard to read, because OutOfRangeError is used as the
    # signal completion
    if not isinstance(e, errors.OutOfRangeError):
        logging.error(str(e))
    raise
