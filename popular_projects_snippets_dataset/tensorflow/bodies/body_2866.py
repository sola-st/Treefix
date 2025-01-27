# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
lhs, lhs_ty = self.visit(node.left)
for op, right in zip(node.ops, node.comparators):
    rhs, rhs_ty = self.visit(right)
    if isinstance(op, ast.Eq):
        pred = 'eq'
    elif isinstance(op, ast.Lt):
        pred = 'ult'
    elif isinstance(op, ast.LtE):
        pred = 'ule'
    elif isinstance(op, ast.Gt):
        pred = 'ugt'
    elif isinstance(op, ast.GtE):
        pred = 'uge'
    elif isinstance(op, ast.NotEq):
        pred = 'ne'
    else:
        raise NotImplementedError('Compare operator not recognized')

    ret = self._ssa_name(pred)
    if lhs_ty == TFRTypes.ATTR:
        self._emit_with_loc(
            '\n{} = tfr.equal {}, {} -> i1'.format(ret, lhs, rhs), node)
    else:
        if lhs_ty == TFRTypes.I64:
            code = 'arith.cmpi'
        elif lhs_ty == TFRTypes.F32:
            code = 'arith.cmpf'
        elif lhs_ty == TFRTypes.INDEX:
            code = 'arith.cmpi'
            # TODO(fengliuai): the reverse type inference should solve the issue.
            rhs, _ = self._i64_to_index(rhs, rhs_ty)
        else:
            raise NotImplementedError('Compare operand type not recognized')
        self._emit_with_loc(
            '\n{} = {} "{}", {}, {} : {}'.format(ret, code, pred, lhs, rhs,
                                                 lhs_ty), node)

    exit((ret, TFRTypes.I1))
