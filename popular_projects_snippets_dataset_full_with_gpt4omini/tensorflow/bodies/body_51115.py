# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.f = def_function.function(
    lambda x: 2. * x,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
options = save_options.SaveOptions(function_aliases={
    "my_func": root.f,
})
save.save(root, save_dir, root.f, options=options)
function_cache = root.f._variable_creation_fn._list_all_concrete_functions()
function_aliases = loader_impl.parse_saved_model(
    save_dir).meta_graphs[0].meta_info_def.function_aliases
self.assertLen(function_cache, 1)
self.assertEqual(function_cache[0].name.decode("utf-8"),
                 list(function_aliases.keys())[0])
