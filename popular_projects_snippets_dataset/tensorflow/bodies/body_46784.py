# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn(a):
        return a.foo
    """

node = templates.replace(template, foo='b')[0]
result, _, _ = loader.load_ast(node)
mod = imp.new_module('test')
mod.b = 3
self.assertEqual(3, result.test_fn(mod))

with self.assertRaises(ValueError):
    templates.replace(template, foo=1)
