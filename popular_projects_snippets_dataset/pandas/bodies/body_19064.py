# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
if isinstance(node.op, (ast.Not, ast.Invert)):
    exit(UnaryOp("~", self.visit(node.operand)))
elif isinstance(node.op, ast.USub):
    exit(self.const_type(-self.visit(node.operand).value, self.env))
elif isinstance(node.op, ast.UAdd):
    raise NotImplementedError("Unary addition not supported")
