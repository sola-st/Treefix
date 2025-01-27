# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
# PREDICT: wrong keys
self._assertInvalidSignature(
    {},
    {"baz": _STRING, "qux": _FLOAT},
    signature_constants.PREDICT_METHOD_NAME)

self._assertInvalidSignature(
    {"foo": _STRING, "bar": _FLOAT},
    {},
    signature_constants.PREDICT_METHOD_NAME)
