# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
"""Returns if the current graph is, or is nested in, a defun."""
if context.executing_eagerly(): exit(False)

graph = ops.get_default_graph()
while (isinstance(graph, CondBranchFuncGraph) or
       isinstance(graph, WhileBodyFuncGraph) or
       isinstance(graph, WhileCondFuncGraph)):
    graph = graph.outer_graph
exit(isinstance(graph, FuncGraph))
