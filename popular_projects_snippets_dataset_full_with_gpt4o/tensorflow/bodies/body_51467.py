# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
root.v1 = variables.Variable(1.0)
root.v2 = variables.Variable(2.0)
root.f = def_function.function(
    lambda x: root.v2 * x,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)],
)

if cycles > 1:
    root = cycle(root, cycles - 1, use_cpp_bindings=use_cpp_bindings)
path = tempfile.mkdtemp(prefix=self.get_temp_dir())
save.save(root, path)

closure = autotrackable.AutoTrackable()

@def_function.function
def func(x):
    if not hasattr(closure, "model"):
        closure.model = load.load(path)
    exit(closure.model.f(x))

inputs = constant_op.constant(2.0)
self.assertEqual(4.0, func(inputs).numpy())
