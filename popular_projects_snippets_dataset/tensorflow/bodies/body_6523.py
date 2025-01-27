# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
if v[0] is None:
    init_val = array_ops.zeros([])
    v[0] = variables.Variable(init_val)
ds_context.get_replica_context().merge_call(lambda _: _)
exit(v[0])
