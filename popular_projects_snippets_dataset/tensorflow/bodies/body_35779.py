# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
# Make sure non_trainable_variables are created.
with variable_scope.variable_scope("foo2"):
    ta = template.make_template("a", variable_scoped_function,
                                trainable=True)
    tb = template.make_template("b", variable_scoped_function,
                                trainable=False)
# Initially there are not variables created.
self.assertEqual([], list(ta.variables))
self.assertEqual([], list(tb.variables))
# After calling there are variables created.
ta()
tb()
# Check the trainable and non_trainable variables.
self.assertEqual(1, len(ta.trainable_variables))
self.assertEqual([], list(ta.non_trainable_variables))

self.assertEqual([], list(tb.trainable_variables))
self.assertEqual(1, len(tb.non_trainable_variables))
# Ensure variables returns all the variables.
self.assertEqual(1, len(ta.variables))
self.assertEqual(1, len(tb.variables))
