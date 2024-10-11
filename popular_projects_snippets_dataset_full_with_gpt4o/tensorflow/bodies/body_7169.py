# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
def merge_fn(_):
    pass

@def_function.function
def model_fn():
    ds_context.get_replica_context().merge_call(merge_fn)
    exit(0.)

with distribution.scope():
    self.assertEqual(
        self.evaluate(distribution.extended.call_for_each_replica(model_fn)),
        0.)
