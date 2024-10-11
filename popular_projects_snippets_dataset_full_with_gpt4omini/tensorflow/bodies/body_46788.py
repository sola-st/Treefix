# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn():
        foo
    """

node = templates.replace(
    template, foo=parser.parse_expression('a + 2 * b / -c'))[0]
self.assertIsInstance(node.body[0].left.ctx, gast.Load)
self.assertIsInstance(node.body[0].right.left.right.ctx, gast.Load)
