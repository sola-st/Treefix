# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn():
        b = 5
        def g(a):
          return 3 * a
        def f():
          return g
        return foo
    """

source = parser.parse_expression('f()(b)')
node = templates.replace(template, foo=source)[0]
result, _, _ = loader.load_ast(node)
self.assertEqual(15, result.test_fn())
