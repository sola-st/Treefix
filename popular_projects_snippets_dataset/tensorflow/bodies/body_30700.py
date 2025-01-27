# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
for (m, n, p, use_gpu) in itertools.product(
    [10],
    [10, 100, 1000, 10000, 100000, 1000000],
    [0.01, 0.5, 0.99],
    [False, True]):
    name = "m_%d_n_%d_p_%g_use_gpu_%s" % (m, n, p, use_gpu)
    device = "/%s:0" % ("gpu" if use_gpu else "cpu")
    with ops.Graph().as_default():
        with ops.device(device):
            x = random_ops.random_uniform((m, n), dtype=dtypes.float32) <= p
            v = resource_variable_ops.ResourceVariable(x)
            op = array_ops.where(v)
        with session.Session(config=benchmark.benchmark_config()) as sess:
            self.evaluate(v.initializer)
            r = self.run_op_benchmark(sess, op, min_iters=100, name=name)
            gb_processed_input = m * n / 1.0e9
            # approximate size of output: m*n*p int64s for each axis.
            gb_processed_output = 2 * 8 * m * n * p / 1.0e9
            gb_processed = gb_processed_input + gb_processed_output
            throughput = gb_processed / r["wall_time"]
            print("Benchmark: %s \t wall_time: %0.03g s \t "
                  "Throughput: %0.03g GB/s" % (name, r["wall_time"], throughput))
            sys.stdout.flush()
