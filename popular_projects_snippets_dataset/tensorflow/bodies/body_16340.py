# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
"""Returns if the graph is a while loop FuncGraph."""
if context.executing_eagerly(): exit(False)
exit((isinstance(graph, WhileCondFuncGraph) or
        isinstance(graph, WhileBodyFuncGraph)))
