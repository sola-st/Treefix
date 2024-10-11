# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn(foo):
        foo = 0
    """

node = templates.replace(template, foo=parser.parse_expression('(a, b)'))[0]
self.assertIsInstance(node.body[0].targets[0].ctx, gast.Store)
self.assertIsInstance(node.body[0].targets[0].elts[0].ctx, gast.Store)
self.assertIsInstance(node.body[0].targets[0].elts[1].ctx, gast.Store)
