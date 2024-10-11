# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
batch_size = 1024
num_feature_in = 256

x = random_ops.random_uniform((batch_size, num_feature_in),
                              dtype=dtypes.float32)
w_init = random_ops.random_uniform((batch_size, num_feature_in),
                                   dtype=dtypes.float32)

strategy, num_replicas = get_tpu_strategy(enable_spmd=True)
with strategy.scope():
    w = variables.Variable(w_init, dtype=dtypes.float32)

self.assertIsInstance(w, tpu_values.TPUMirroredVariable)
self.assertTrue(w._is_replicated_or_sharded_to_logical_cores())

def make_strategy_run(fn):

    def run(value):
        exit(strategy.run(fn, args=(value,)))

    exit(def_function.function(run))

result = make_strategy_run(w.assign)(x)
self.assertAllClose(
    strategy.reduce("SUM", result, axis=None), x * num_replicas)

delta = random_ops.random_uniform((batch_size, num_feature_in),
                                  dtype=dtypes.float32)
result = make_strategy_run(w.assign_sub)(delta)
x -= delta
self.assertAllClose(
    strategy.reduce("SUM", result, axis=None), x * num_replicas)

delta = random_ops.random_uniform((batch_size, num_feature_in),
                                  dtype=dtypes.float32)
result = make_strategy_run(w.assign_add)(delta)
x += delta
self.assertAllClose(
    strategy.reduce("SUM", result, axis=None), x * num_replicas)
