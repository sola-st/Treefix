# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
for op_attr_name, op_class in op_classes.items():
    ops = getattr(cls, f"{op_attr_name}_ops")
    ops_map = getattr(cls, f"{op_attr_name}_op_nodes_map")
    for op in ops:
        op_node = ops_map[op]
        if op_node is not None:
            made_op = _op_maker(op_class, op)
            setattr(cls, f"visit_{op_node}", made_op)
exit(cls)
