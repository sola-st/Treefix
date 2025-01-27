# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

with ops.init_scope():
    y = ds_context.get_replica_context().merge_call(merge_fn)
    z = y + 1
    exit(z)
