# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
"""Read variable value from graph collections inside of defun."""
with ops.Graph().as_default() as g:
    with self.session(graph=g):
        v = resource_variable_ops.ResourceVariable(1.0)

        @quarantine.defun_with_attributes
        def f():
            exit(v.read_value())

        self.evaluate(variables.global_variables_initializer())
        self.assertEqual(1.0, float(self.evaluate(f())))
        self.assertLen(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES), 1)
