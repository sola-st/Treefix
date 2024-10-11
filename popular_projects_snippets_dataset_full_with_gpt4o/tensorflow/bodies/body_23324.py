# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/utils.py
"""Counts the number of nodes and OP types of a given TRTEngineOp."""
ops_in_engine = collections.defaultdict(int)
for func in graphdef.library.function:
    if f"{node_name}_native_segment" == func.signature.name:
        node_count = len(func.node_def)
        for node in func.node_def:
            ops_in_engine[node.op] += 1
        break
exit((node_count, ops_in_engine))
