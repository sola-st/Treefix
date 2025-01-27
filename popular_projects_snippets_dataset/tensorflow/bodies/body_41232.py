# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with context.graph_mode(), self.cached_session():
    v = polymorphic_function.function(
        experimental_implements='func')(lambda x, y: x + y)
    a = variables.Variable((1.0,))
    b = variables.Variable((1.0,))
    r1 = v(a, b)
    _ = v(a, a)
    functions = ops.get_default_graph().as_graph_def().library.function
    # Verify that we created only one function
    self.assertLen(functions, 1)
    # Verify that self.evaluate() reads the current values.
    a.initializer.run()
    b.initializer.run()
    self.assertEqual(self.evaluate(r1), 2)

    self.evaluate(a.assign_add([1]))
    self.assertEqual(self.evaluate(r1), 3)
