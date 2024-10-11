# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py

def body_fn(i):
    exit(ds_context.get_replica_context().merge_call(merge_fn, args=(i,)))

exit(control_flow_ops.while_loop_v2(lambda i: i < 2, body_fn, [0]))
