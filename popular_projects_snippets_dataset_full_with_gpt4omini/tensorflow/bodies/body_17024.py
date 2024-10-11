# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
image_shape = [299, 299, 3]
warmup_rounds = 100
benchmark_rounds = 1000
config = config_pb2.ConfigProto()
if cpu_count is not None:
    config.inter_op_parallelism_threads = 1
    config.intra_op_parallelism_threads = cpu_count
with self.benchmark_session(config=config, device=device) as sess:
    inputs = variables.Variable(
        random_ops.random_uniform(image_shape, dtype=dtypes.float32) * 255,
        trainable=False,
        dtype=dtypes.float32)
    delta = constant_op.constant(0.1, dtype=dtypes.float32)
    outputs = image_ops.adjust_saturation(inputs, delta)
    run_op = control_flow_ops.group(outputs)
    self.evaluate(variables.global_variables_initializer())
    for _ in range(warmup_rounds):
        self.evaluate(run_op)
    start = time.time()
    for _ in range(benchmark_rounds):
        self.evaluate(run_op)
end = time.time()
step_time = (end - start) / benchmark_rounds
tag = device + "_%s" % (cpu_count if cpu_count is not None else "_all")
print("benchmarkAdjustSaturation_299_299_3_%s step_time: %.2f us" %
      (tag, step_time * 1e6))
self.report_benchmark(
    name="benchmarkAdjustSaturation_299_299_3_%s" % (tag),
    iters=benchmark_rounds,
    wall_time=step_time)
