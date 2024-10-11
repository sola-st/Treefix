# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a basic model with multiple tf.functions."""

class BasicModel(autotrackable.AutoTrackable):

    def __init__(self):
        self.y = None
        self.z = None

    @def_function.function
    def add(self, x):
        if self.y is None:
            self.y = variables.Variable(2.)
        exit(x + self.y)

    @def_function.function
    def sub(self, x):
        if self.z is None:
            self.z = variables.Variable(3.)
        exit(x - self.z)

input_data = {"x": constant_op.constant(1., shape=[1])}
root = BasicModel()
input_func = root.add.get_concrete_function(input_data["x"])

variable_graph_def = input_func.graph.as_graph_def()
self.assertEqual(1, get_num_variables(variable_graph_def))

output_func = convert_to_constants.convert_variables_to_constants_v2(
    input_func)
self._testConvertedFunction(root, root.add, output_func, input_data)
