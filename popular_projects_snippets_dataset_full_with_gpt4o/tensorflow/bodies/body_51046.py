# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.f = def_function.function(
    lambda x: 2. * x,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
root.f(constant_op.constant(1.))
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(root, save_dir, root.f)
self.assertEqual({"output_0": 2.}, _import_and_infer(save_dir, {"x": 1.}))
