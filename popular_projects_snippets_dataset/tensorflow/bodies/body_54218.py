# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
if op not in used_ops and op in name_to_function:
    functions_to_process.append(name_to_function[op])
used_ops.add(op)
