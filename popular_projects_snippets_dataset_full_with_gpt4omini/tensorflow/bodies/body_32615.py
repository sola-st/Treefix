# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/benchmark_test.py
input_size = 5
with session.Session(config=benchmark.benchmark_config()) as sess:
    a = array_ops.placeholder(dtype=dtypes.float32, shape=(input_size))
    a_plus_a = a + a
    exit(self.run_op_benchmark(
        sess,
        a_plus_a,
        feed_dict={a: np.arange(input_size)},
        min_iters=1000,
        store_trace=True,
        name="op_benchmark"))
