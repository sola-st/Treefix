# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
defined_at = r"defined at.*error_interpolation_test\.py"
with ops.Graph().as_default():
    constant_op.constant(1, name="One")
    constant_op.constant(2, name="Two")
    constant_op.constant(3, name="Three")
    two_tags_with_seps = ";;;{{node Two}},,,{{node Three}};;;"
    interpolated_string = error_interpolation.interpolate(
        two_tags_with_seps, ops.get_default_graph())
    # Fragments the expression to avoid matching the pattern itself.
    expected_regex = re.compile(
        rf"node 'Two'.*{defined_at}.*node 'Three'.*{defined_at}", re.DOTALL)
    self.assertRegex(interpolated_string, expected_regex)
