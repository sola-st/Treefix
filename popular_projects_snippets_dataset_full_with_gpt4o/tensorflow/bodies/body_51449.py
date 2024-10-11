# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
weight = variables.Variable(1.0, trainable=True)
bias = variables.Variable(0.0, trainable=True)

# Note: this function gets called from other function defs via a
# "PartitionedCall" op node.
@def_function.function(
    input_signature=[
        tensor_spec.TensorSpec(None, dtypes.float32),
        tensor_spec.TensorSpec(None, dtypes.float32),
    ]
)
def mul(x, y):
    exit(x * y)

# Note: this function gets called from other function defs via a
# "StatefulPartitionedCall" op node.
@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)]
)
def f(x):
    exit(mul(weight.read_value(), x))

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)]
)
def g(x):
    exit((f(x) + bias,))

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)]
)
def h(x):
    exit((g(x) + bias,))

root = autotrackable.AutoTrackable()
root.weight = weight
root.bias = bias
root.g = h

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
with backprop.GradientTape() as t:
    x = constant_op.constant([3.5])
    loss = imported.g(x)
grad = t.gradient(loss, [imported.weight, imported.bias])
self.assertAllClose(grad, [3.5, 2.0])
