# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
batch_size = 32
num_feature_in = 16

x = random_ops.random_uniform((batch_size, num_feature_in),
                              dtype=dtypes.float32)
w_init = random_ops.random_uniform((batch_size, num_feature_in),
                                   dtype=dtypes.float32)

strategy, _ = get_tpu_strategy(enable_spmd=True)
with strategy.scope():
    w = variables.Variable(w_init, dtype=dtypes.float32)

w.assign(x)
result = w.numpy()
self.assertAllClose(result, x)

x1 = random_ops.random_uniform((batch_size, num_feature_in),
                               dtype=dtypes.float32)
w.assign_sub(x1)
result = w.numpy()
self.assertAllClose(result, x - x1)

x2 = random_ops.random_uniform((batch_size, num_feature_in),
                               dtype=dtypes.float32)
w.assign(x)
w.assign_add(x2)
result = w.numpy()
self.assertAllClose(result, x + x2)
