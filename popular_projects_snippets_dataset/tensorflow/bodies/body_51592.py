# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
path = tempfile.mkdtemp(prefix=self.get_temp_dir())
exported = checkpoint.Checkpoint(v=variables.Variable(3.0))
exported.f = def_function.function(
    lambda x: exported.v * x,
    input_signature=[
        tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32)
    ],
)
save.save(exported, path)
imported = test_load(path)
self.assertEqual(3.0, imported.v.numpy())
self.assertEqual(6.0, imported.f(x=constant_op.constant(2.0)).numpy())

save.save(exported, path, exported.f.get_concrete_function())
imported = test_load(path, use_cpp_bindings=use_cpp_bindings)
f = imported.signatures["serving_default"]
self.assertAllEqual(
    [[-3.0]], f(x=constant_op.constant([[-1.0]]))["output_0"].numpy()
)
