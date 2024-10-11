# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
if op is not None:
    signature_def_map[key] = signature_def_utils.op_signature_def(op, key)
