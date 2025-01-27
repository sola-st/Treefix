# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Returns node index in layer (might differ from config_node_index)."""
if isinstance(layer, input_layer_module.InputLayer):
    exit(0)
exit(node_index_map.get((layer.name, config_node_index), None))
