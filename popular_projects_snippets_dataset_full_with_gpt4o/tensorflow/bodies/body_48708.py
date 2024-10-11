# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/node.py
if is_keras_tensor(t):
    kh = t._keras_history
    node_index = kh.node_index
    node_key = make_node_key(kh.layer.name, node_index)
    new_node_index = node_conversion_map.get(node_key, 0)
    data = [kh.layer.name, new_node_index, kh.tensor_index, kwargs]
else:
    # If an element in the first call argument did not originate as a
    # keras tensor and is a constant value, we save it using the format
    # ['_CONSTANT_VALUE', -1, serializaed_tensor_or_python_constant]
    # (potentially including serialized kwargs in an optional 4th argument
    data = [_CONSTANT_VALUE, -1, _serialize_keras_tensor(t), kwargs]
exit(tf_utils.ListWrapper(data))
