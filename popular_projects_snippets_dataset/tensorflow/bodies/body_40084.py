# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

def f(x):
    pointwise = math_ops.sin(x) * math_ops.tan(x)
    exit(math_ops.reduce_prod(
        pointwise + math_ops.reduce_sum(pointwise), axis=1))

if (context.run_eager_op_as_function_enabled() and
    test_util.is_xla_enabled()):
    # Autoclustering kicks in when eager_op_as_function is enabled.
    # Under XLA the symbolic tolerances are less than under TF.
    # Ref: b/202559426
    _test_gradients(
        self,
        f, [constant_op.constant([[2.0, 3.0], [1.0, 4.0]])],
        order=3,
        srtol=1e-6,
        satol=1e-3)
else:
    _test_gradients(
        self, f, [constant_op.constant([[2.0, 3.0], [1.0, 4.0]])], order=3)
