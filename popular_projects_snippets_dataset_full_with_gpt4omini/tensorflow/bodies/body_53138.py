# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
if op.device:
    exit(op.device)
exit("/cpu:0" if op.node_def.op in ["Variable", "VariableV2"] else op.device)
