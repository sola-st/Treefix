# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
num_iters = 100
shape = [int(1e6)]
randn_dt, uniform_dt = randn_sampler_switchover(shape, num_iters, use_gpu)

print(("Randn Sampler vs uniform samplers [%d iters]\t%.4f\t%.4f") %
      (num_iters, randn_dt, uniform_dt))

gpu_str = "_gpu" if use_gpu else "_cpu"
self.report_benchmark(
    name="randn_sampler" + gpu_str, iters=num_iters, wall_time=randn_dt)
self.report_benchmark(
    name="uniform_sampler" + gpu_str, iters=num_iters, wall_time=uniform_dt)
