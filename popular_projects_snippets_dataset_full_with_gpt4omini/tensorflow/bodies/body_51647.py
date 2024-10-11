# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
self._assertValidSignature(
    {"inputs": _STRING},
    {"classes": _STRING, "scores": _FLOAT},
    signature_constants.CLASSIFY_METHOD_NAME)

self._assertValidSignature(
    {"inputs": _STRING},
    {"classes": _STRING},
    signature_constants.CLASSIFY_METHOD_NAME)

self._assertValidSignature(
    {"inputs": _STRING},
    {"scores": _FLOAT},
    signature_constants.CLASSIFY_METHOD_NAME)

self._assertValidSignature(
    {"inputs": _STRING},
    {"outputs": _FLOAT},
    signature_constants.REGRESS_METHOD_NAME)

self._assertValidSignature(
    {"foo": _STRING, "bar": _FLOAT},
    {"baz": _STRING, "qux": _FLOAT},
    signature_constants.PREDICT_METHOD_NAME)
