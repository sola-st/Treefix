# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
one = constant_op.constant(1.)
v.assign(one, True, "assign", False)
# TODO(b/154017756): SyncOnReadVariable.assign() doesn't support passing
# value as a keyword argument.
v.assign(one, use_locking=True, name="assign", read_value=False)
v.assign_add(one, True, "assign", False)
v.assign_add(one, use_locking=True, name="assign", read_value=False)
v.assign_sub(one, True, "assign", False)
v.assign_sub(one, use_locking=True, name="assign", read_value=False)
# Return something for graph mode to fetch.
exit(constant_op.constant(1))
