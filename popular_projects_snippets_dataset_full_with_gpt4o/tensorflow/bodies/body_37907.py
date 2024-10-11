# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduce_benchmark_test.py
config = config_pb2.ConfigProto(
    graph_options=config_pb2.GraphOptions(
        optimizer_options=config_pb2.OptimizerOptions(
            opt_level=config_pb2.OptimizerOptions.L0)))
with ops.Graph().as_default(), session.Session(config=config) as sess:

    with ops.device("/cpu:0"):
        tensor = constant_op.constant(np.zeros([100, 1000], dtype=np.float32))
        reduction = math_ops.reduce_sum(tensor)
        grad, = gradients_impl.gradients(reduction, tensor)

    def fn():
        self.evaluate(grad.op)

    self._run(fn, 10000)
