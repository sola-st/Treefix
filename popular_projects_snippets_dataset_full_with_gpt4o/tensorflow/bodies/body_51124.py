# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = checkpoint.Checkpoint(v=variables.Variable(2.))
root.f = def_function.function(
    lambda x: 2. * root.v,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
export_dir = os.path.join(self.get_temp_dir(), "save_dir")

@def_function.function
def _calls_save():
    save.save(root, export_dir)

with self.assertRaisesRegex(AssertionError, "tf.function"):
    _calls_save()
