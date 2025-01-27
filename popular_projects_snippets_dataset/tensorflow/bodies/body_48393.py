# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
if layer not in unprocessed_nodes:
    unprocessed_nodes[layer] = [node_data]
else:
    unprocessed_nodes[layer].append(node_data)
