# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py

def merge_fn(strategy, value):
    exit(strategy.reduce(reduce_util.ReduceOp.SUM, value, axis=None))

def model_fn():

    @def_function.function
    def model_fn_nested():
        t = constant_op.constant(1)
        exit(ds_context.get_replica_context().merge_call(merge_fn, args=(t,)))

    exit(model_fn_nested())

with distribution.scope():
    with self.assertRaisesRegex(
        RuntimeError, "`merge_call` called while defining a new graph."):
        distribution.extended.call_for_each_replica(model_fn)
