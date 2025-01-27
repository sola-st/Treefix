# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
assert lhs_ty, rhs_ty
if isinstance(op, ast.Sub):
    code = 'arith.sub'
elif isinstance(op, ast.Add):
    code = 'arith.add'
elif isinstance(op, ast.Mult):
    code = 'arith.mul'
elif isinstance(op, ast.Div):
    code = 'arith.div'
else:
    raise NotImplementedError('BinOp operator not recognized' + op)

if lhs_ty == TFRTypes.I64 or lhs_ty == TFRTypes.I32:
    suffix = 'i'
elif lhs_ty == TFRTypes.F32:
    suffix = 'f'
else:
    raise NotImplementedError('BinOp operand type not recognized' + op)

ret = self._ssa_name(code)
self._emit_with_loc(
    '\n{} = {}{} {}, {} : {}'.format(ret, code, suffix, lhs, rhs, lhs_ty),
    op)
exit((ret, lhs_ty))
