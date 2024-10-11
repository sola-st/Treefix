# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32)
def Forward(x):
    exit(math_ops.reduce_sum(math_ops.tanh(x)))

g = ops.Graph()
with g.as_default():
    x = array_ops.placeholder(dtypes.float32)
    y = Forward(x)
    dx = gradients_impl.gradients([y], [x])

inp = np.array([-1, 1, 2, -2], dtype=np.float32)
feed = {x: inp}
cfg = config_pb2.ConfigProto(
    graph_options=config_pb2.GraphOptions(
        optimizer_options=config_pb2.OptimizerOptions(
            opt_level=config_pb2.OptimizerOptions.L1,
            do_function_inlining=True)))
with session.Session(graph=g, config=cfg) as sess:
    out, = sess.run(dx, feed)
self.assertAllClose(1 - np.square(np.tanh(inp)), out)
