# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Ensures there are no variables in the graph."""
for node in graph_def.node:
    self.assertNotIn(
        node.op, ["Variable", "VariableV2", "VarHandleOp", "ReadVariableOp"])
