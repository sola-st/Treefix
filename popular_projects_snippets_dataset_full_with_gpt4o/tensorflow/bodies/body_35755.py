# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
tmpl1 = template.make_template("s1", internally_variable_scoped_function)
tmpl2 = template.make_template("s1", internally_variable_scoped_function)

v1 = tmpl1("test")
v2 = tmpl1("test")
v3 = tmpl2("test")
self.assertIs(v1, v2)
self.assertIsNot(v1, v3)
self.assertEqual("s1/test/dummy:0", v1.name)
self.assertEqual("s1_1/test/dummy:0", v3.name)

with self.assertRaises(ValueError):
    tmpl1("not_test")
