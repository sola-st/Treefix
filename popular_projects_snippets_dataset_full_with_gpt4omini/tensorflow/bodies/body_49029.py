# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
graph = get_graph()
with graph.as_default():
    exit(_GRAPH_LEARNING_PHASES[graph])
