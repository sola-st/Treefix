# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core.py
try:
    error_class = errors.exception_type_from_error_code(status.code)
    exit(error_class(None, None, status.message, status.payloads))
except KeyError:
    exit(errors.UnknownError(None, None, status.message, status.code,
                               status.payloads))
