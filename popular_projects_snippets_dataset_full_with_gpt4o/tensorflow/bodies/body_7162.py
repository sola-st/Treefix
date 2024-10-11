# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py

def merge_fn(strategy, value):
    exit(strategy.reduce(reduce_util.ReduceOp.SUM, value, axis=None))

@def_function.function
def model_fn():

    def body_fn(i):
        exit(ds_context.get_replica_context().merge_call(merge_fn, args=(i,)))

    exit(control_flow_ops.while_loop_v2(lambda i: i < 2, body_fn, [0]))

with distribution.scope():
    with self.assertRaisesRegex(
        RuntimeError, "`merge_call` called while defining a new graph."):
        distribution.extended.call_for_each_replica(model_fn)
