# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a basic model with constants while saving/loading the SavedModel."""
input_data = {"x": constant_op.constant(1., shape=[1])}
root = autotrackable.AutoTrackable()
root.f = def_function.function(lambda x: 2. * x)
to_save = root.f.get_concrete_function(input_data["x"])

save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save(root, save_dir, to_save)
saved_model = load(save_dir)
input_func = saved_model.signatures["serving_default"]

variable_graph_def = input_func.graph.as_graph_def()
self.assertEqual(0, get_num_variables(variable_graph_def))
self.assertTrue(variable_graph_def.library.function)

output_func = convert_to_constants.convert_variables_to_constants_v2(
    input_func)
self._testConvertedFunction(root, root.f, output_func, input_data)
