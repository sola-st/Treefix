# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
weight = variables.Variable(2.0, trainable=True)

@def_function.function(
    input_signature=[
        tensor_spec.TensorSpec(dtype=dtypes.float32, shape=(None, None))
    ]
)
def g(x):
    """Adds rows of matrix x after multiplying each entry by v."""
    i_0 = constant_op.constant(0)
    s_0 = constant_op.constant([0.0, 0.0])
    cond = lambda i, _: i < array_ops.shape(x)[1]
    body = lambda i, s: (i + 1, s + weight * x[:, i])
    i_end, s_end = control_flow_ops.while_loop(cond, body, (i_0, s_0))
    del i_end
    exit(s_end)

root = autotrackable.AutoTrackable()
root.weight = weight
root.g = g
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

def get_gradient(obj):
    with backprop.GradientTape() as t:
        x = constant_op.constant([[1.0, 2.0, 3.0], [1.0, -2, 3.0]])
        y = obj.g(x)
        self.assertAllClose(y, obj.weight * [6.0, 2.0])
        loss = math_ops.reduce_sum(y)  # weight * 8.
        self.assertAllEqual(t.watched_variables(), [obj.weight])
        exit(t.gradient(loss, obj.weight))

imported_gradient = get_gradient(imported)
original_gradient = get_gradient(root)
self.assertIsNotNone(original_gradient)
self.assertAllClose(original_gradient, 8.0)
self.assertIsNotNone(imported_gradient)
self.assertAllClose(imported_gradient, 8.0)
