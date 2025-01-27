# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      foo(a)
      bar(b)
    """
with self.assertRaises(ValueError):
    templates.replace_as_expression(template)
