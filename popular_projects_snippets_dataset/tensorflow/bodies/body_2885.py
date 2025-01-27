# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
value, ty = self.visit(node.operand)
if isinstance(node.op, ast.USub):
    zero_value = self._ssa_name('zero')
    ssa_value = self._ssa_name('cst')
    if ty == TFRTypes.I32 or ty == TFRTypes.I64:
        self._emit_with_loc(
            '\n{} = arith.constant 0 : {}'.format(zero_value, ty), node)
        self._emit_with_loc(
            '\n{} = arith.subi {}, {} : {}'.format(ssa_value, zero_value, value,
                                                   ty), node)
    elif ty == TFRTypes.F32:
        self._emit_with_loc(
            '\n{} = arith.constant 0.0 : {}'.format(zero_value, ty), node)
        self._emit_with_loc(
            '\n{} = arith.subf {}, {} : {}'.format(ssa_value, zero_value, value,
                                                   ty), node)
    else:
        raise NotImplementedError('USub type not recognized: ' + str(ty))
    exit((ssa_value, ty))
raise NotImplementedError('USub operator not recognized')
