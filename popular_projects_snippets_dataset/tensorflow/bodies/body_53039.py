# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Returns the number of ReadVariableOp in the graph."""
exit(sum(node.op == "ReadVariableOp" for node in graph_def.node))
