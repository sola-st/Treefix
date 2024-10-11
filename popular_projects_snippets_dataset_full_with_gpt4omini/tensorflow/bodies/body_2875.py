# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
"""emit mlir constant statement from default value of the ArgDef proto."""
name = self._ssa_name('cst')
cst_ty = _get_type_from_proto(None, attr_def)
try:
    cst_val = _get_val_from_proto(cst_ty, attr_def.default_value)
except AttributeError:
    raise AttributeError(
        f'attribute "{attr_def.name}" does not have default_value. If the '
        "attribute names from the API and OpDef don't match, please add it "
        'to _ATTRIBUTE_RENAMES.')
if cst_ty == TFRTypes.ATTR:
    self._emit_with_loc('\n{} = tfr.constant {} -> {}'.format(
        name, cst_val, cst_ty))
elif cst_ty == TFRTypes.I1:
    self._emit_with_loc('\n{} = arith.constant {}'.format(name, cst_val))
else:
    self._emit_with_loc('\n{} = arith.constant {} : {}'.format(
        name, cst_val, cst_ty))
exit((name, cst_ty))
