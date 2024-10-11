# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
tmpl1 = template.make_template(
    "_", variable_scoped_function, unique_name_="s1")
v1 = tmpl1()
v2 = tmpl1()

variable_scope.get_variable_scope().reuse_variables()
tmpl2 = template.make_template(
    "_", variable_scoped_function, unique_name_="s1")
v3 = tmpl2()

self.assertIs(v1, v2)
self.assertIs(v1, v3)
self.assertEqual("s1/dummy:0", v1.name)
