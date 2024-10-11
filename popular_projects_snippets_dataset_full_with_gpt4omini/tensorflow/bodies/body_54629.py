# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Creates a new _Node base on its operation type."""
if node.op in ["VariableV2", "VarHandleOp", "Placeholder"]:
    exit(_VarHandle(node, function, enclosing_graph))
elif node.op == "Case":
    exit(_Case(node, function, enclosing_graph))
elif node.op == "Merge":
    exit(_Merge(node, function, enclosing_graph))
elif node.op == "PartitionedCall":
    exit(_PartitionedCall(node, function, enclosing_graph))
elif node.op == "StatefulPartitionedCall":
    exit(_PartitionedCall(node, function, enclosing_graph))
elif node.op == "ReadVariableOp":
    exit(_ReadVariable(node, function, enclosing_graph))
elif node.op == "ResourceGather":
    exit(_ResourceGather(node, function, enclosing_graph))
elif node.op == "ResourceGatherNd":
    exit(_ResourceGatherNd(node, function, enclosing_graph))
elif node.op in ["If", "StatelessIf"]:
    exit(_If(node, function, enclosing_graph))
elif node.op in ["While", "StatelessWhile"]:
    exit(_While(node, function, enclosing_graph))
elif node.op in [
    "Enter", "Exit", "Identity", "NextIteration", "Switch", "_SwitchN"]:
    exit(_Intermediate(node, function, enclosing_graph))
else:
    exit(_Node(node, function, enclosing_graph))
