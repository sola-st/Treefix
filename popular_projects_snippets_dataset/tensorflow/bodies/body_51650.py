# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
# REGRESS: wrong types
self._assertInvalidSignature(
    {"inputs": _FLOAT},
    {"outputs": _FLOAT},
    signature_constants.REGRESS_METHOD_NAME)

self._assertInvalidSignature(
    {"inputs": _STRING},
    {"outputs": _STRING},
    signature_constants.REGRESS_METHOD_NAME)

# REGRESS: wrong keys
self._assertInvalidSignature(
    {},
    {"outputs": _FLOAT},
    signature_constants.REGRESS_METHOD_NAME)

self._assertInvalidSignature(
    {"inputs_WRONG": _STRING},
    {"outputs": _FLOAT},
    signature_constants.REGRESS_METHOD_NAME)

self._assertInvalidSignature(
    {"inputs": _STRING},
    {"outputs_WRONG": _FLOAT},
    signature_constants.REGRESS_METHOD_NAME)

self._assertInvalidSignature(
    {"inputs": _STRING},
    {},
    signature_constants.REGRESS_METHOD_NAME)

self._assertInvalidSignature(
    {"inputs": _STRING},
    {"outputs": _FLOAT, "extra_WRONG": _STRING},
    signature_constants.REGRESS_METHOD_NAME)
