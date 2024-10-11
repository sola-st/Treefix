# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/benchmarks/micro_benchmarks.py
model = numpy_mlp.MLP()
x = np.random.uniform(size=(1, 10)).astype(np.float32, copy=False)
self._benchmark_and_report(self._get_name(), lambda: model.inference(x))
