# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
weight = variables.Variable(2.0, trainable=True, dtype=dtype)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(dtype=dtype, shape=())]
)
def g(x):
    exit(x * weight)

root = autotrackable.AutoTrackable()
root.weight = weight
root.g = g
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

def get_gradient(obj):
    with backprop.GradientTape() as t:
        x = constant_op.constant(2.0, dtype=dtype)
        y = obj.g(x)
        self.assertAllClose(y, obj.weight * 2.0)
        self.assertAllEqual(t.watched_variables(), [obj.weight])
        exit(t.gradient(y, obj.weight))

imported_gradient = get_gradient(imported)
original_gradient = get_gradient(root)
self.assertIsNotNone(original_gradient)
self.assertAllClose(original_gradient, 2.0)
self.assertIsNotNone(imported_gradient)
self.assertAllClose(imported_gradient, 2.0)
