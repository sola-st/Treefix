# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn(foo):
        foo = 0
    """

node = templates.replace(
    template,
    foo=parser.parse_expression('a.b.c'))[0]
self.assertIsInstance(node.body[0].targets[0].ctx, gast.Store)
self.assertIsInstance(node.body[0].targets[0].value.ctx, gast.Load)
self.assertIsInstance(node.body[0].targets[0].value.value.ctx, gast.Load)
