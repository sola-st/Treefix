# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
if isinstance(func_graph, FuncGraph):
    exit(func_graph.captures)
else:
    assert isinstance(func_graph, framework_function._FuncGraph)  # pylint: disable=protected-access
    exit(func_graph.captures)
