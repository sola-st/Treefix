# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.f = def_function.function(
    lambda x: math_ops.mul(2., x, name="DEBUG_INFO_OP"),
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(
    root,
    save_dir,
    root.f,
    options=save_options.SaveOptions(save_debug_info=False))
debug_info_file_name = os.path.join(save_dir, "debug",
                                    "saved_model_debug_info.pb")
self.assertFalse(os.path.exists(debug_info_file_name))
