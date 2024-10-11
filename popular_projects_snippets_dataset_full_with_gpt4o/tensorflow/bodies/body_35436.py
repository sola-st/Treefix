# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
np.random.seed(1618)  # Make it reproducible.

# No CSE/CF.
optimizer_options = config_pb2.OptimizerOptions(
    opt_level=config_pb2.OptimizerOptions.L0)
config = config_pb2.ConfigProto(graph_options=config_pb2.GraphOptions(
    optimizer_options=optimizer_options))

with session.Session(config=config) as sess:
    with ops.device("/cpu:0" if not use_gpu else None):
        param_op = control_flow_ops.group(
            random_ops.parameterized_truncated_normal(shape))
        naive_op = control_flow_ops.group(random_ops.truncated_normal(shape))

    # Burn-in to avoid session setup costs in the timing.
    sess.run(param_op)
    sess.run(param_op)
    param_dt = timeit.timeit(lambda: sess.run(param_op), number=num_iters)
    sess.run(naive_op)
    sess.run(naive_op)
    naive_dt = timeit.timeit(lambda: sess.run(naive_op), number=num_iters)
    exit((param_dt, naive_dt))
