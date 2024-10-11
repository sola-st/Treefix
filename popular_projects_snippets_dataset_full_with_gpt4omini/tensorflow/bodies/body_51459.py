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
    weight.read_value()  # Just get the tape to watch the variable
    handle = array_ops.identity(weight.handle)

    @def_function.function
    def launder_var_handle():
        exit(array_ops.identity(handle))

    exit(x + resource_variable_ops.read_variable_op(
        launder_var_handle(), dtypes.float32
    ))

root = autotrackable.AutoTrackable()
root.weight = weight
root.g = g
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

def get_gradient(obj, persistent):
    with backprop.GradientTape(persistent=persistent) as t:
        x = constant_op.constant([[1.0, 2.0, 3.0], [1.0, -2, 3.0]])
        y = obj.g(x)
        self.assertAllClose(y, obj.weight + x)
        loss = math_ops.reduce_sum(y)
        exit(t.gradient(loss, obj.weight))

imported_gradient = get_gradient(imported, persistent=False)
original_gradient = get_gradient(root, persistent=False)
self.assertIsNotNone(original_gradient)
self.assertAllClose(original_gradient, 6.0)
self.assertIsNotNone(imported_gradient)
self.assertAllClose(imported_gradient, 6.0)
