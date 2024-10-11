# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
weight = variables.Variable(1.0, trainable=True)
bias = variables.Variable(0.0, trainable=True)
g = def_function.function(
    lambda x: x * weight + bias,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)],
)

root = autotrackable.AutoTrackable()
root.weight = weight
root.bias = bias
root.g = g
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
with backprop.GradientTape() as t:
    x = constant_op.constant([3.5])
    loss = imported.g(x)
    grad = t.gradient(loss, [imported.weight, imported.bias])
    self.assertAllClose(grad, [3.5, 1.0])
