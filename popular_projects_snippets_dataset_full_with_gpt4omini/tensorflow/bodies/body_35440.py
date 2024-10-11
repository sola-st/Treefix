# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
num_iters = 50
print(("Composition of new ParameterizedTruncatedNormalOp vs. "
       "naive TruncatedNormalOp [%d iters]") % num_iters)
print("Shape\tsec(parameterized)\tsec(naive)\tspeedup")

for shape in [[10000, 100], [1000, 1000], [1000000], [100, 100, 100],
              [20, 20, 20, 20]]:
    p_dt, n_dt = parameterized_vs_naive(shape, num_iters, use_gpu)
    print("%s\t%.3f\t%.3f\t%.2f" % (shape, p_dt, n_dt, p_dt / n_dt))

    shape_str = "-".join(map(str, shape))
    self.report_benchmark(
        name="parameterized_shape" + shape_str,
        iters=num_iters,
        wall_time=p_dt)
    self.report_benchmark(
        name="naive_shape" + shape_str, iters=num_iters, wall_time=n_dt)
