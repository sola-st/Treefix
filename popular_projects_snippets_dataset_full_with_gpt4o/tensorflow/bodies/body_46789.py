# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn():
        foo = 0
    """

node = templates.replace(
    template, foo=parser.parse_expression('bar(([a, b],)).baz'))[0]
self.assertIsInstance(node.body[0].targets[0].ctx, gast.Store)
function_call_arg = node.body[0].targets[0].value.args[0]
self.assertIsInstance(function_call_arg.elts[0].ctx, gast.Load)
self.assertIsInstance(function_call_arg.elts[0].elts[0].ctx, gast.Load)
self.assertIsInstance(function_call_arg.elts[0].elts[1].ctx, gast.Load)
