# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
exit(hasattr(x, "graph") and getattr(x.graph, "name", None) == "keras_graph")
