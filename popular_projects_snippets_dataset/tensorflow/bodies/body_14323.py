# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/benchmarks/micro_benchmarks.py
with tf.device('/CPU:0'):
    model = tf_numpy_mlp.MLP()
    x = tfnp.ones(shape=(1, 10)).astype(np.float32)
    self._benchmark_and_report(
        self._get_name(), tf.function(lambda: model.inference(x)))
