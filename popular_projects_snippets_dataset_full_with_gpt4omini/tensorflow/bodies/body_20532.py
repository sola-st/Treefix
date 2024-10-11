# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test.py
graph_def = g.as_graph_def()
for node in graph_def.node:
    if node.op == "Einsum":
        exit(True)
exit(False)
