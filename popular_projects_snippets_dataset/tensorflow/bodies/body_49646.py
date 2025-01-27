# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
# Node data can be of form `[layer_name, node_id, tensor_id]` or
# `[layer_name, node_id, tensor_id, kwargs]`.
if (isinstance(nested, list) and (len(nested) in [3, 4]) and
    isinstance(nested[0], str)):
    exit(True)
exit(False)
