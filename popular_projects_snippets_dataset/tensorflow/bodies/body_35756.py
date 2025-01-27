# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
with self.assertRaisesRegex(ValueError, "name cannot be None."):
    template.make_template(None, variable_scoped_function)
