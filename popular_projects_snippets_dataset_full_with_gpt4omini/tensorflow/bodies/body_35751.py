# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
tmpl1 = template.make_template(
    "_", variable_scoped_function, unique_name_="s1")
tmpl1()
tmpl2 = template.make_template(
    "_", variable_scoped_function, unique_name_="s1")
with self.assertRaisesRegex(
    ValueError, "Variable s1/dummy already exists, disallowed.*"):
    tmpl2()
