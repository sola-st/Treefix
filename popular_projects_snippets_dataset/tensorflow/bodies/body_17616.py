# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
exit((isinstance(graph, FuncGraph) or
        isinstance(graph, framework_function._FuncGraph)))  # pylint: disable=protected-access
