# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn():
        def f(a, d, f):
          return a + d + f
        return f(1, kws=None)
    """

source = parser.parse_expression('f(d=3, f=5)')
node = templates.replace(template, kws=source.keywords)[0]
result, _, _ = loader.load_ast(node)
self.assertEqual(9, result.test_fn())

with self.assertRaises(ValueError):
    templates.replace(template, kws=[])
    templates.replace(template, kws=1)
