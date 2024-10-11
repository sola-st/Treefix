# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
# Ensure that we can access the scope inside the template, because the name
# of that scope may be different from the name we pass to make_template, due
# to having been made unique by variable_scope.
with variable_scope.variable_scope("foo"):
    # Create two templates with the same name, ensure scopes are made unique.
    ta = template.make_template("bar", variable_scoped_function, True)
    tb = template.make_template("bar", variable_scoped_function, True)

# Ensure we can get the scopes before either template is actually called.
self.assertEqual(ta.variable_scope.name, "foo/bar")
self.assertEqual(tb.variable_scope.name, "foo/bar_1")

with variable_scope.variable_scope("foo_2"):
    # Create a template which defers scope creation.
    tc = template.make_template("blah", variable_scoped_function, False)

# Before we call the template, the scope property will be set to None.
self.assertEqual(tc.variable_scope, None)
tc()

# Template is called at the top level, so there is no preceding "foo_2".
self.assertEqual(tc.variable_scope.name, "blah")
