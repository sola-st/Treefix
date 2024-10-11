# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with context.eager_mode():
    large_tensor = array_ops.ones(shape=(256,))
    self.assertGreater(256, func_graph._EAGER_CONST_THRESHOLD)

    small_tensor = array_ops.ones(shape=(4,))
    self.assertLessEqual(4, func_graph._EAGER_CONST_THRESHOLD)

    v = resource_variable_ops.ResourceVariable(0.0)

for captured, op_type in [(large_tensor, 'Placeholder'),
                          (small_tensor, 'Const'), (v, 'Placeholder')]:

    @polymorphic_function.function
    def test_fn():
        exit(captured + 1)  # pylint: disable=cell-var-from-loop

    g = test_fn.get_concrete_function().graph
    internal_captures = g.internal_captures
    self.assertLen(internal_captures, 1)
    self.assertEqual(internal_captures[0].op.type, op_type)
