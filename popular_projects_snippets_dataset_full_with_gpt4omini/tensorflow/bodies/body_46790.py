# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn():
        foo = 0
    """

node = templates.replace(
    template, foo=parser.parse_expression('foo(a[b]).bar'))[0]
function_call_arg = node.body[0].targets[0].value.args[0]
self.assertIsInstance(function_call_arg.ctx, gast.Load)
self.assertIsInstance(function_call_arg.slice.ctx, gast.Load)
