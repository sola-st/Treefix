# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/benchmarks/micro_benchmarks.py
sizes = [(100,), (10000,), (1000000,)]
repeats = [FLAGS.repeat] * 2 + [10]
times = []
for size, repeat in zip(sizes, repeats):
    x = np.random.uniform(size=size).astype(np.float32, copy=False)
    name = '{}_{}'.format(self._get_name(), size)
    times.append(self._benchmark_np_and_tf_np(name, op, (x,), repeat))
self._print_times(op, sizes, times)
