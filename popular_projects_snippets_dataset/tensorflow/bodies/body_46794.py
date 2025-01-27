# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      foo(a)
    """

node = templates.replace_as_expression(template, foo='bar', a='baz')
self.assertIsInstance(node, gast.Call)
self.assertEqual(node.func.id, 'bar')
self.assertEqual(node.args[0].id, 'baz')
