# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
with context.eager_mode():
    tmpl = template.make_template("s",
                                  function_with_side_create,
                                  trainable=False)
    self.assertIs(tmpl(name="1"), tmpl(name="2"))
