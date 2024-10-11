# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      a = foo(arg)
    """
source = parser.parse_expression('[lambda i: i]')
node = templates.replace(template, arg=source)
lambda_arg = node[0].value.args[0].elts[0]
self.assertIsInstance(lambda_arg.args.args[0].ctx, gast.Param)
self.assertIsInstance(lambda_arg.body.ctx, gast.Load)
