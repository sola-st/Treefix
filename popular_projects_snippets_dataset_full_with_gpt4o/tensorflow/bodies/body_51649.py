# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
# CLASSIFY: wrong types
self._assertInvalidSignature(
    {"inputs": _FLOAT},
    {"classes": _STRING, "scores": _FLOAT},
    signature_constants.CLASSIFY_METHOD_NAME)

self._assertInvalidSignature(
    {"inputs": _STRING},
    {"classes": _FLOAT, "scores": _FLOAT},
    signature_constants.CLASSIFY_METHOD_NAME)

self._assertInvalidSignature(
    {"inputs": _STRING},
    {"classes": _STRING, "scores": _STRING},
    signature_constants.CLASSIFY_METHOD_NAME)

# CLASSIFY: wrong keys
self._assertInvalidSignature(
    {},
    {"classes": _STRING, "scores": _FLOAT},
    signature_constants.CLASSIFY_METHOD_NAME)

self._assertInvalidSignature(
    {"inputs_WRONG": _STRING},
    {"classes": _STRING, "scores": _FLOAT},
    signature_constants.CLASSIFY_METHOD_NAME)

self._assertInvalidSignature(
    {"inputs": _STRING},
    {"classes_WRONG": _STRING, "scores": _FLOAT},
    signature_constants.CLASSIFY_METHOD_NAME)

self._assertInvalidSignature(
    {"inputs": _STRING},
    {},
    signature_constants.CLASSIFY_METHOD_NAME)

self._assertInvalidSignature(
    {"inputs": _STRING},
    {"classes": _STRING, "scores": _FLOAT, "extra_WRONG": _STRING},
    signature_constants.CLASSIFY_METHOD_NAME)
