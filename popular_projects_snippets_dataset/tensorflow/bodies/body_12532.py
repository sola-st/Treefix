# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
assign_fn = lambda var, r_value: var.assign(
    r_value, use_locking=use_locking, name=name, read_value=read_value)
assign_list = self._apply_assign_fn(assign_fn, value)
if read_value:
    exit(assign_list)
exit([assign.op for assign in assign_list])
