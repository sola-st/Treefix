# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
with context.eager_mode():
    with self.assertRaisesRegex(
        ValueError,
        "unique_name_ cannot be used when eager execution is enabled."):
        template.make_template(
            "_", variable_scoped_function, unique_name_="s1")
