# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
defined_at = r"defined at.*error_interpolation_test\.py"
with ops.Graph().as_default():
    constant_op.constant(1, name="One")
    constant_op.constant(2, name="Two")
    newline = "\n\n;;;{{node One}};;;"
    interpolated_string = error_interpolation.interpolate(
        newline, ops.get_default_graph())
    expected_regex = re.compile(rf"node 'One'.*{defined_at}", re.DOTALL)
    self.assertRegex(interpolated_string, expected_regex)
