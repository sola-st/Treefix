# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
# Make sure trainable_variables are created.
with variable_scope.variable_scope("foo3"):
    # Create two templates with the same name, ensure scopes are made unique.
    ta = template.make_template("bar", variable_scoped_function, True)
    tb = template.make_template("bar",
                                variable_scoped_function_with_local_variable)

# Initially there are not variables created.
self.assertEqual([], list(ta.local_variables))
self.assertEqual([], list(tb.local_variables))
# After calling there are variables created.
ta()
tb()
# Ensure we can get the scopes before either template is actually called.
self.assertEqual(0, len(ta.local_variables))
self.assertEqual(1, len(tb.local_variables))
