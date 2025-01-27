# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
with ops.Graph().as_default():
    constant_op.constant(1, name="One")
    normal_string = "This is just a normal string"
    interpolated_string = error_interpolation.interpolate(
        normal_string, ops.get_default_graph())
    self.assertIn(normal_string, interpolated_string)
