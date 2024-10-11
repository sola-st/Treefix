# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
tmpl = template.make_template("s",
                              function_with_side_create,
                              trainable=True)

tmpl(name="1")
with self.assertRaises(ValueError):
    tmpl(name="2")
