# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
signature_def = signature_def_utils_impl.build_signature_def(
    inputs, outputs, method_name)
self.assertFalse(
    signature_def_utils_impl.is_valid_signature(signature_def))
