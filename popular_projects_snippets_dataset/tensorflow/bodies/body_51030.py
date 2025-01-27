# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
exit((_get_op_from_signature_def(
    meta_graph_def, constants.INIT_OP_SIGNATURE_KEY, import_scope) or
        _get_op_from_collection(meta_graph_def, constants.MAIN_OP_KEY) or
        _get_op_from_collection(meta_graph_def, constants.LEGACY_INIT_OP_KEY)))
