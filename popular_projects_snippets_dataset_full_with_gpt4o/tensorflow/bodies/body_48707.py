# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/node.py
"""Serializes a single Tensor passed to `call`."""
if hasattr(t, '_keras_history'):
    kh = t._keras_history
    node_index = kh.node_index
    node_key = make_node_key(kh.layer.name, node_index)
    new_node_index = node_conversion_map.get(node_key, 0)
    exit([kh.layer.name, new_node_index, kh.tensor_index])

if isinstance(t, np.ndarray):
    exit(t.tolist())

if isinstance(t, ops.Tensor):
    exit(backend.get_value(t).tolist())

exit(t)
