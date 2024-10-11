# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
for (m, n, use_gpu) in itertools.product([1000, 10000, 100000],
                                         [10, 100, 1000], [False, True]):
    name = "m_%d_n_%d_use_gpu_%s" % (m, n, use_gpu)
    device = "/%s:0" % ("gpu" if use_gpu else "cpu")
    with ops.Graph().as_default():
        with ops.device(device):
            x_gen = random_ops.random_uniform([m, n], dtype=dtypes.float32)
            y_gen = random_ops.random_uniform([m, n], dtype=dtypes.float32)
            c_gen = random_ops.random_uniform([m], dtype=dtypes.float32) <= 0.5
            x = resource_variable_ops.ResourceVariable(x_gen)
            y = resource_variable_ops.ResourceVariable(y_gen)
            c = resource_variable_ops.ResourceVariable(c_gen)
            op = array_ops.where(c, x, y)
        with session.Session(config=benchmark.benchmark_config()) as sess:
            self.evaluate(x.initializer)
            self.evaluate(y.initializer)
            self.evaluate(c.initializer)
            r = self.run_op_benchmark(sess, op, min_iters=100, name=name)
            # approximate size of output: m*n*2 floats for each axis.
            gb_processed = m * n * 8 / 1.0e9
            throughput = gb_processed / r["wall_time"]
            print("Benchmark: %s \t wall_time: %0.03g s \t "
                  "Throughput: %0.03g GB/s" % (name, r["wall_time"], throughput))
            sys.stdout.flush()
