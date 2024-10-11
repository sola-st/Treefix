# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
tpl = template.make_template("", variable_scoped_function)
with variable_scope.variable_scope("outer"):
    x = variable_scope.get_variable("x", [])
    v = tpl()
self.assertEqual("outer/", tpl.variable_scope_name)
self.assertEqual("outer//dummy:0", v.name)
if context.executing_eagerly():
    # In eager mode `x` is not visible to the template since the template does
    # not rely on global collections.
    self.assertEqual(1, len(tpl.variables))
    self.assertIs(v, tpl.variables[0])
else:
    self.assertEqual([x, v], tpl.variables)
