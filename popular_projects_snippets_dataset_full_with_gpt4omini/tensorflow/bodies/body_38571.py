# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
for (m, n, p, use_gpu) in itertools.product(
    [128],
    [10, 100, 1000, 10000, 100000],
    [0.001, 0.01, 0.5, 0.99, 1.0],
    [False, True]):
    k = int(p * n)
    if k == 0:
        continue
    name = "m_%d_n_%d_k_%g_use_gpu_%s" % (m, n, k, use_gpu)
    device = "/%s:0" % ("gpu" if use_gpu else "cpu")
    with ops.Graph().as_default():
        with ops.device(device):
            x = random_ops.random_uniform((m, n))
            v = resource_variable_ops.ResourceVariable(x)
            op = nn_ops.top_k(v, k)
        with session.Session() as sess:
            self.evaluate(v.initializer)
            r = self.run_op_benchmark(sess, op, min_iters=100, name=name)
            gb_processed_input = m * n / 1.0e9
            throughput = gb_processed_input / r["wall_time"]
            print("Benchmark: %s \t wall_time: %0.03g s \t "
                  "Throughput: %0.03g GB/s" % (name, r["wall_time"], throughput))
            sys.stdout.flush()
