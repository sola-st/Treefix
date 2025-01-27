# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
# Test both that we can call it with positional and keywords.
tmpl1 = template.make_template(
    "s1", internally_variable_scoped_function, scope_name="test")
tmpl2 = template.make_template(
    "s1", internally_variable_scoped_function, scope_name="test")

v1 = tmpl1()
v2 = tmpl1()
v3 = tmpl2()
self.assertIs(v1, v2)
self.assertIsNot(v1, v3)
self.assertEqual("s1/test/dummy:0", v1.name)
self.assertEqual("s1_1/test/dummy:0", v3.name)
