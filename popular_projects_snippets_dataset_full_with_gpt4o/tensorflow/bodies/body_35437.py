# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
# Benchmark by constructing samplers on the threshold of using the randn
# rejection sampling and check that this threshold is set correctly by
# benchmarking with bounds just above and below this threshold.
# The uniform and randn samplers should have about the same performance
# at this point.

stddev_inside_bounds_before_using_randn = (
    _get_stddev_inside_bounds_before_using_randn(use_gpu))

epsilon = 0.001

np.random.seed(1618)  # Make it reproducible.

# No CSE/CF.
optimizer_options = config_pb2.OptimizerOptions(
    opt_level=config_pb2.OptimizerOptions.L0)
config = config_pb2.ConfigProto(
    graph_options=config_pb2.GraphOptions(
        optimizer_options=optimizer_options))

with session.Session(config=config) as sess:
    with ops.device("/cpu:0" if not use_gpu else "/gpu:0"):
        uniform_sampler_op = control_flow_ops.group(
            random_ops.parameterized_truncated_normal(
                shape,
                means=0.,
                stddevs=1.0,
                minvals=-stddev_inside_bounds_before_using_randn + epsilon,
                maxvals=0.01))
        randn_sampler_op = control_flow_ops.group(
            random_ops.parameterized_truncated_normal(
                shape,
                means=0.,
                stddevs=1.0,
                minvals=-stddev_inside_bounds_before_using_randn - epsilon,
                maxvals=0.01))

    # Burn-in to avoid session setup costs in the timing.
    sess.run(uniform_sampler_op)
    sess.run(uniform_sampler_op)
    uniform_dt = timeit.timeit(
        lambda: sess.run(uniform_sampler_op), number=num_iters)

    sess.run(randn_sampler_op)
    sess.run(randn_sampler_op)
    randn_dt = timeit.timeit(
        lambda: sess.run(randn_sampler_op), number=num_iters)

    exit((randn_dt, uniform_dt))
