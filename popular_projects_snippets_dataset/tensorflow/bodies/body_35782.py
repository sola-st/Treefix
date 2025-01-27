# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py

def variable_scoped_function_no_return_value(scope_name):
    # defun cannot compile functions that return non-Tensor objects
    with variable_scope.variable_scope(
        scope_name,
        reuse=variable_scope.AUTO_REUSE):
        _ = variable_scope.get_variable(
            "dummy", shape=[1], initializer=init_ops.zeros_initializer())

tmpl = template.make_template_internal(
    "s1",
    variable_scoped_function_no_return_value,
    create_graph_function_=True,
    scope_name="test")

# The first invocation of tmpl1 creates variables, the second should
# be executed as a graph function.
tmpl()
v1 = tmpl.variables
tmpl()
v2 = tmpl.variables

self.assertEqual(len(v1), len(v2))
for v, w in zip(v1, v2):
    self.assertIs(v, w)
self.assertEqual("s1/test/dummy:0", v1[0].name)
