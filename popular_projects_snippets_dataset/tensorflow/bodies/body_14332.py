# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/benchmarks/micro_benchmarks.py
sizes = [(2, 2), (10, 10), (100, 100), (200, 200), (1000, 1000)]
# Override repeat flag since this can be very slow.
repeats = [FLAGS.repeat] * 3 + [50, 10]
times = []
for size, repeat in zip(sizes, repeats):
    x = np.random.uniform(size=size).astype(np.float32, copy=False)
    name = '{}_{}'.format(self._get_name(), size)
    times.append(
        self._benchmark_np_and_tf_np(name, 'matmul', (x, x), repeat=repeat))

self._print_times('matmul', sizes, times)
