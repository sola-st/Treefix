# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with context.graph_mode(), self.cached_session():
    v = polymorphic_function.function(
        experimental_implements='func')(lambda x, y: x + y)
    a = variables.Variable(1.0)
    r1 = v(a, 2.)
    r2 = v(2., a)
    functions = ops.get_default_graph().as_graph_def().library.function
    self.assertLen(functions, 1)
    self.assertLen(functions[0].signature.input_arg, 2)
    # Verify that self.evaluate() reads the current values.
    a.initializer.run()
    self.assertEqual(self.evaluate(r1), 3)
    self.assertEqual(self.evaluate(r2), 3)
