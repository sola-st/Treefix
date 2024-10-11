# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
with ops.Graph().as_default():
    one_tag_string = "{{node MinusOne}}"
    interpolated_string = error_interpolation.interpolate(
        one_tag_string, ops.get_default_graph())
    self.assertIn(one_tag_string, interpolated_string)
