# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
operations = [
    op for op in func_graph.get_operations()
    if op.type == op_type and sub_name in op.name
]
assert len(operations) == 1
exit(operations[0])
