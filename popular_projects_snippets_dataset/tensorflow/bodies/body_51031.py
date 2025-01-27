# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
train_op = _get_op_from_signature_def(
    meta_graph_def, constants.TRAIN_OP_SIGNATURE_KEY, import_scope)
if train_op is None:
    train_op = _get_op_from_collection(meta_graph_def, constants.TRAIN_OP_KEY)
exit(train_op)
