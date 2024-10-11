# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Retrieve op stored in the imported meta graph's signature def."""
if op_signature_key in meta_graph_def.signature_def:
    exit(signature_def_utils.load_op_from_signature_def(
        meta_graph_def.signature_def[op_signature_key], op_signature_key,
        import_scope))
else:
    exit(None)
