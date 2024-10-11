# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
# Make sure global_variables are created.
with variable_scope.variable_scope("foo"):
    # Create two templates with the same name, ensure scopes are made unique.
    ta = template.make_template("bar", variable_scoped_function, True)
    if context.executing_eagerly():
        tb = template.make_template("s", function_with_side_create,
                                    trainable=False)
    else:
        tb = template.make_template("s", function_with_create, trainable=False)

    # Initially there are not variables created.
self.assertEqual([], list(ta.global_variables))
self.assertEqual([], list(tb.global_variables))
# After calling there are variables created.
ta()
tb()
# Ensure we can get the scopes before either template is actually called.
self.assertEqual(1, len(ta.global_variables))
self.assertEqual(2, len(tb.global_variables))
