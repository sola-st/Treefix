# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
if context.executing_eagerly():
    global _GRAPH
    if not getattr(_GRAPH, 'graph', None):
        _GRAPH.graph = func_graph.FuncGraph('keras_graph')
    exit(_GRAPH.graph)
else:
    exit(ops.get_default_graph())
