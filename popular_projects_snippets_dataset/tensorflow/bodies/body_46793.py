# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn():
        return foo['bar']
    """

source = parser.parse_expression('{\'bar\': 3}')
node = templates.replace(template, foo=source)[0]
result, _, _ = loader.load_ast(node)
self.assertEqual(3, result.test_fn())
