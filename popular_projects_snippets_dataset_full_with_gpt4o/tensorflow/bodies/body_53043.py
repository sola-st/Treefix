# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a basic model with Variables."""
input_data = {"x": constant_op.constant(1., shape=[1])}
root = autotrackable.AutoTrackable()
root.v1 = variables.Variable(3.)
root.v2 = variables.Variable(2.)
root.f = def_function.function(lambda x: root.v1 * root.v2 * x)
input_func = root.f.get_concrete_function(input_data["x"])

variable_graph_def = input_func.graph.as_graph_def()
self.assertEqual(2, get_num_variables(variable_graph_def))

output_func = convert_to_constants.convert_variables_to_constants_v2(
    input_func)
self._testConvertedFunction(root, root.f, output_func, input_data)
