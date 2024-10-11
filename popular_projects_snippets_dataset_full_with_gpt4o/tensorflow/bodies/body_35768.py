# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
# Create templates in scope a then call in scope b. make_template should
# capture the scope the first time it is called, and make_immediate_template
# should capture the scope at construction time.
with variable_scope.variable_scope("ctor_scope"):
    # Create scope here:
    tmpl_immed = template.make_template("a", variable_scoped_function,
                                        True)
    # default: create scope at __call__
    tmpl_defer = template.make_template(
        "b", variable_scoped_function, False)
with variable_scope.variable_scope("call_scope"):
    inner_imm_var = tmpl_immed()
    inner_defer_var = tmpl_defer()
outer_imm_var = tmpl_immed()
outer_defer_var = tmpl_defer()

self.assertIsNot(inner_imm_var, inner_defer_var)
self.assertIs(outer_imm_var, inner_imm_var)
self.assertIs(outer_defer_var, inner_defer_var)

self.assertEqual("ctor_scope/a/dummy:0", inner_imm_var.name)
self.assertEqual("call_scope/b/dummy:0", inner_defer_var.name)
