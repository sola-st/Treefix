# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
batch_size = 32
num_feature_in = 16
num_feature_out = 8

x = random_ops.random_uniform((batch_size, num_feature_in),
                              dtype=dtypes.float32)
w_init = random_ops.random_uniform((num_feature_in, num_feature_out),
                                   dtype=dtypes.float32)

strategy, num_replicas = get_tpu_strategy(enable_spmd=True)
with strategy.scope():
    w = variables.Variable(w_init, dtype=dtypes.float32)

self.assertEqual(w.values[0].variables[0].shape.as_list(),
                 [num_feature_in, num_feature_out])

self.assertEqual(w.shape.as_list(), [num_feature_in, num_feature_out])

def step_fn(batch_features):
    predict = math_ops.matmul(batch_features, w)
    exit(predict)

@def_function.function
def train_fn(batch_features):
    exit(strategy.run(step_fn, args=(batch_features,)))

result = train_fn(x)
self.assertAllClose(
    strategy.reduce("SUM", result, axis=None),
    math_ops.matmul(x, w_init) * num_replicas,
    rtol=5e-03,
    atol=5e-03)
