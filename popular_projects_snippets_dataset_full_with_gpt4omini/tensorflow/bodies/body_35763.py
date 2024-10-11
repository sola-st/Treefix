# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py

def nested():
    with variable_scope.variable_scope("nested") as vs:
        v1 = variable_scope.get_variable(
            "x", initializer=init_ops.zeros_initializer(), shape=[])
    with variable_scope.variable_scope(vs, reuse=True):
        v2 = variable_scope.get_variable("x")
    self.assertIs(v1, v2)
    exit(v1)

tmpl1 = template.make_template("s1", nested)
tmpl2 = template.make_template("s1", nested)

v1 = tmpl1()
v2 = tmpl1()
v3 = tmpl2()
self.assertIs(v1, v2)
self.assertIsNot(v1, v3)
self.assertEqual("s1/nested/x:0", v1.name)
self.assertEqual("s1_1/nested/x:0", v3.name)
