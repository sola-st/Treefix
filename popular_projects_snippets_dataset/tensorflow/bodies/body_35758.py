# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
tmpl = template.make_template("s", function_with_create, trainable=True)

tmpl()
with self.assertRaises(ValueError):
    tmpl()
