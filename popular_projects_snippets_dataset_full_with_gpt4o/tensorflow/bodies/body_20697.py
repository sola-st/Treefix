# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
node_map = {}
for node in nodes:
    node_map[node.name] = node
exit(node_map)
