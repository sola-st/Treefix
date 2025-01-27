# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(noinline=True)
def Foo(x):
    exit(x * 2)

self.assertTrue(
    Foo.instantiate([dtypes.float32]).definition.attr["_noinline"].b)

g = ops.Graph()
with g.as_default():
    x = constant_op.constant(3.0)
    y = Foo(x)
    dx, = gradients_impl.gradients(y, [x])

cfg = config_pb2.ConfigProto(
    graph_options=config_pb2.GraphOptions(
        optimizer_options=config_pb2.OptimizerOptions(
            opt_level=config_pb2.OptimizerOptions.L0,
            do_common_subexpression_elimination=True,
            do_function_inlining=True,
            do_constant_folding=True)))

with self.session(graph=g, config=cfg):
    self.assertAllClose(y, 6.)
    self.assertAllClose(dx, 2.)
