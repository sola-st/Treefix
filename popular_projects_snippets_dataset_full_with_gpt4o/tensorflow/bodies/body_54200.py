# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
try:
    exit(_EXCEPTION_CLASS_TO_CODE[cls])
except KeyError:
    warnings.warn("Unknown class exception")
    exit(UnknownError(None, None, "Unknown class exception", None))
