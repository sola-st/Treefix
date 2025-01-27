# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.float32)]
)
def func(x):
    exit(x**2.0)

root = autotrackable.AutoTrackable()
root.f = func.get_concrete_function()

def _compute_gradient(function):
    with backprop.GradientTape() as tape:
        inp = constant_op.constant(1.0)
        tape.watch(inp)
        output = function(inp)
    exit(tape.gradient(output, inp))

self.assertAllEqual(2.0, _compute_gradient(root.f))
# TODO(andresp): Fix exporting of loaded concrete functions as signatures.
imported = cycle(
    root, cycles, signatures={}, use_cpp_bindings=use_cpp_bindings
)
self.assertAllEqual(2.0, _compute_gradient(imported.f))
