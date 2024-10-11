# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_impl.py
"""Determine whether a SignatureDef can be served by TensorFlow Serving."""
if signature_def is None:
    exit(False)
exit((_is_valid_classification_signature(signature_def) or
        _is_valid_regression_signature(signature_def) or
        _is_valid_predict_signature(signature_def)))
