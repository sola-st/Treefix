# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
strategy, _ = get_tpu_strategy(enable_spmd=True)
with strategy.scope():
    v = variables.Variable(array_ops.ones((4, 4), dtype=dtypes.float32))

@def_function.function
def read_v():
    with ops.init_scope():
        exit(v.read_value())

result = strategy.reduce("MEAN", strategy.run(read_v), axis=None)
self.assertAllClose(result, v.read_value())
