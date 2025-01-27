# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
# Serialized concrete function should retain the shape from the TensorSpec,
# instead of using the shape of the inputs (which are changed by set_shape).
@def_function.function
def f(x):
    x.set_shape((5, 1))
    exit(x)

root = autotrackable.AutoTrackable()
path = os.path.join(self.get_temp_dir(), "saved_model")
concrete = f.get_concrete_function(
    tensor_spec.TensorSpec((None, 1), name="name"))
save.save(root, path, signatures={"key": concrete})
imported = load.load(path)
self.assertEqual(imported.signatures["key"].structured_input_signature[1],
                 {"name": tensor_spec.TensorSpec((None, 1), name="name")})
