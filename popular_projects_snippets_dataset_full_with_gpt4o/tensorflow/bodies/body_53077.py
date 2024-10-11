# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test the raised exception in Eager mode."""
input_data = {"x": constant_op.constant(1., shape=[1])}
root = autotrackable.AutoTrackable()
root.v1 = variables.Variable(3.)
root.v2 = variables.Variable(2.)
root.f = def_function.function(lambda x: root.v1 * root.v2 * x)
input_func = root.f.get_concrete_function(input_data["x"])

with self.assertRaisesRegex(RuntimeError,
                            "must be carried out in a Session"):
    convert_to_constants.convert_var_to_const_function_in_v1(
        input_func)
