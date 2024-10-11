# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
if len(node.body) != 1:
    raise SyntaxError("only a single expression is allowed")
expr = node.body[0]
exit(self.visit(expr, **kwargs))
