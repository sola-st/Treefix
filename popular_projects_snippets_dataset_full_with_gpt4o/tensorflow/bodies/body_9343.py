# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer.py
"""Helper to serialize a graph to string."""
if graph:
    exit(graph.as_graph_def(add_shapes=True).SerializeToString())
else:
    exit(b'')
