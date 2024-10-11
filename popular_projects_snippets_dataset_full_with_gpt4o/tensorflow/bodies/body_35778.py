# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
# Make sure trainable_variables are created.
with variable_scope.variable_scope("foo2"):
    # Create two templates with the same name, ensure scopes are made unique.
    ta = template.make_template("bar", variable_scoped_function, True)
    tb = template.make_template("bar", variable_scoped_function, True)

# Initially there are not variables created.
self.assertEqual([], list(ta.trainable_variables))
self.assertEqual([], list(tb.trainable_variables))
# After calling there are variables created.
ta()
tb()
# Ensure we can get the scopes before either template is actually called.
self.assertEqual(1, len(ta.trainable_variables))
self.assertEqual(1, len(tb.trainable_variables))
# None non-trainable variable was created.
self.assertEqual([], list(ta.non_trainable_variables))
self.assertEqual([], list(tb.non_trainable_variables))
# Ensure variables returns all the variables.
self.assertEqual(1, len(ta.variables))
self.assertEqual(1, len(tb.variables))
