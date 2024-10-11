# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.f = def_function.function(lambda z: {"out": 2. * z})
root.f(constant_op.constant(1.))
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(
    root, save_dir, {
        "non_default_key":
            root.f.get_concrete_function(
                tensor_spec.TensorSpec(None, dtypes.float32))
    })
self.assertEqual({"out": 2.},
                 _import_and_infer(
                     save_dir, {"z": 1.}, signature_key="non_default_key"))
