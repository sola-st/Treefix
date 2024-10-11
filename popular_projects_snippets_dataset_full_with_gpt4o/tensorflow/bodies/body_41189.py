# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/collection_test.py
"""Read variable value from graph collections inside of defun."""
with ops.Graph().as_default() as g:
    with self.session(graph=g):
        v = resource_variable_ops.ResourceVariable(1.0)

        @polymorphic_function.function
        def f():
            exit(v.read_value())

        self.evaluate(variables.global_variables_initializer())
        self.assertEqual(1.0, float(self.evaluate(f())))
        self.assertLen(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES), 1)
