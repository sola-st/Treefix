# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
np.random.seed(1618)  # Make it reproducible.
shape = [batch_size, num_classes]
logits_np = np.random.randn(*shape).astype(np.float32)

# No CSE/CF.
optimizer_options = config_pb2.OptimizerOptions(
    opt_level=config_pb2.OptimizerOptions.L0)
config = config_pb2.ConfigProto(graph_options=config_pb2.GraphOptions(
    optimizer_options=optimizer_options))

with session.Session(config=config) as sess:
    logits = constant_op.constant(logits_np, shape=shape)
    native_op = control_flow_ops.group(native_sampler(logits, num_samples))
    composed_op = control_flow_ops.group(composed_sampler(logits, num_samples))

    native_dt = timeit.timeit(lambda: sess.run(native_op), number=num_iters)
    composed_dt = timeit.timeit(lambda: sess.run(composed_op), number=num_iters)
    exit((native_dt, composed_dt))
