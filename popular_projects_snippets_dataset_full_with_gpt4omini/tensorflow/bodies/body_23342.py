# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
# TODO(laigd): currently we use the collection key to filter out
# collections that depend on variable ops, but this may miss some
# other user-defined collections. A better way would be to use
# CollectionDef::NodeList for the filtering.
collections_to_remove = (
    ops.GraphKeys._VARIABLE_COLLECTIONS + [
        ops.GraphKeys.TRAIN_OP, ops.GraphKeys.WHILE_CONTEXT,
        ops.GraphKeys.COND_CONTEXT
    ])
exit([key for key in collection_keys if key not in collections_to_remove])
