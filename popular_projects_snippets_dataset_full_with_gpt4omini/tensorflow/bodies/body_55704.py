# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
defined_at = r"defined at.*error_interpolation_test\.py"
with ops.Graph().as_default():
    constant_op.constant(1, name="One")
    constant_op.constant(2, name="Two")
    one_tag_with_a_fake_function_tag = "{{function_node fake}}{{node One}}"
    interpolated_string = error_interpolation.interpolate(
        one_tag_with_a_fake_function_tag, ops.get_default_graph())
    # Fragments the expression to avoid matching the pattern itself.
    expected_regex = re.compile(rf"node 'One'.*{defined_at}", re.DOTALL)
    self.assertRegex(interpolated_string, expected_regex)
    self.assertNotIn("function_node", interpolated_string)
    self.assertNotIn("node 'Two'", interpolated_string)
