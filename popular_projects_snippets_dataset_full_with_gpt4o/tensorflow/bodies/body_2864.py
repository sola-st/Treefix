# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
values = [self.visit(value) for value in node.values]
# TODO(fengliuai): Handle more ast node types.
if isinstance(node.op, ast.Or):
    raise NotImplementedError('Or operator not recognized')
elif isinstance(node.op, ast.And):
    raise NotImplementedError('And operator not recognized')
