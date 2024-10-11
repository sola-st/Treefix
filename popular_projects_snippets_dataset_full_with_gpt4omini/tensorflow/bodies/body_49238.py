# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
if context.executing_eagerly():
    exit(_DUMMY_EAGER_GRAPH.key)
else:
    exit(ops.get_default_graph())
