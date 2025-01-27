# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
"""Write variable value inside defun."""
with ops.Graph().as_default() as g:
    with self.session(graph=g):

        @quarantine.defun_with_attributes
        def f():
            v = resource_variable_ops.ResourceVariable(2.0)
            exit(v)

        _ = f.get_concrete_function()
        self.evaluate(variables.global_variables_initializer())
        self.assertEqual(2.0, float(self.evaluate(f())))
        self.assertLen(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES), 1)
