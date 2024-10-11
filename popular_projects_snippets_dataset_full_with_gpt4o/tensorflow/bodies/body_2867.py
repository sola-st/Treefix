# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
cst_name = self._ssa_name('cst')
if node.value is None:
    cst_ty = TFRTypes.NONE
elif isinstance(node.value, bool):
    cst_ty = self._get_inferred_type(node)
    cst_val = str(node.value).lower()
    self._emit_with_loc('\n{} = arith.constant {}'.format(cst_name, cst_val),
                        node)
else:
    cst_ty = self._get_inferred_type(node)
    cst_val = node.value
    if cst_ty == TFRTypes.ATTR:
        self._emit_with_loc(
            '\n{} = tfr.constant "{}" -> {}'.format(cst_name, cst_val, cst_ty),
            node)
    else:
        self._emit_with_loc(
            '\n{} = arith.constant {} : {}'.format(cst_name, cst_val, cst_ty),
            node)
exit((cst_name, cst_ty))
