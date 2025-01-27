# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
# WRONG METHOD
self._assertInvalidSignature(
    {"inputs": _STRING},
    {"classes": _STRING, "scores": _FLOAT},
    "WRONG method name")
