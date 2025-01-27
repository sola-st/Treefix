# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/pretty_printer_test.py
node = ast.FunctionDef(
    name='f',
    args=ast.arguments(
        args=[ast.Name(id='a', ctx=ast.Param())],
        vararg=None,
        kwarg=None,
        defaults=[]),
    body=[
        ast.Return(
            ast.BinOp(
                op=ast.Add(),
                left=ast.Name(id='a', ctx=ast.Load()),
                right=ast.Num(1)))
    ],
    decorator_list=[],
    returns=None)
# Just checking for functionality, the color control characters make it
# difficult to inspect the result.
self.assertIsNotNone(pretty_printer.fmt(node))
