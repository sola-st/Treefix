# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      a = foo(func, args)
    """
source = parser.parse_expression('bar(*[i for i in range(j)])')
node = templates.replace(template, func=source.func, args=source.args)
arg_node = node[0].value.args[1].value
self.assertIsInstance(arg_node.generators[0].target.ctx, gast.Store)
self.assertIsInstance(arg_node.elt.ctx, gast.Load)
