# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
# Benchmark the first iteration of a conv-net with many identical conv
# operations.
if not test.is_gpu_available():
    exit()

with ops.Graph().as_default(), session_lib.Session() as session:
    batch_size = 1
    timesteps = 600
    features = 1

    inputs = random_ops.random_uniform(
        [batch_size, 1, timesteps, features], seed=1234)
    num_outputs_list = [512] * 40 + [1]
    kernel_w = 3
    x = inputs
    for num_outputs in num_outputs_list:
        x = convolutional.conv2d(x, num_outputs, [1, kernel_w])
    outputs = x

    self.evaluate(variables.global_variables_initializer())
    num_iterations = 4
    for iter_index in range(num_iterations):
        start = time.time()
        session.run(outputs)
        wall_time = time.time() - start
        self.report_benchmark(
            name="conv_stack_iter_%d" % iter_index, wall_time=wall_time)
        tf_logging.info("conv_stack_iter_%d: %.4f" % (iter_index, wall_time))
