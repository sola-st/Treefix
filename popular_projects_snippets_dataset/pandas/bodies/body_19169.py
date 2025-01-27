# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
ops = node.ops
comps = node.comparators

# base case: we have something like a CMP b
if len(comps) == 1:
    op = self.translate_In(ops[0])
    binop = ast.BinOp(op=op, left=node.left, right=comps[0])
    exit(self.visit(binop))

# recursive case: we have a chained comparison, a CMP b CMP c, etc.
left = node.left
values = []
for op, comp in zip(ops, comps):
    new_node = self.visit(
        ast.Compare(comparators=[comp], left=left, ops=[self.translate_In(op)])
    )
    left = comp
    values.append(new_node)
exit(self.visit(ast.BoolOp(op=ast.And(), values=values)))
