# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
arg_strs = []
arg_tys = []
for arg in args:
    value, ty = self.visit(arg)
    arg_strs.append(value)
    arg_tys.append(ty)
tfr_op_name = 'tfr.' + op_name[5:]
ret_tys = (
    TFR_BUILTINS[op_name](*arg_tys)
    if callable(TFR_BUILTINS[op_name]) else TFR_BUILTINS[op_name])
# Convert the tfr builtin returns to a list.
if isinstance(ret_tys, tuple):
    ret_tys = list(ret_tys)
else:
    ret_tys = [ret_tys]

ret_str, ret_ssa_values = self._get_mlir_ssa_values(op_name, ret_tys)

arg_str = ', '.join(arg_strs)
arg_ty_str = ', '.join(str(ty) for ty in arg_tys)
ret_ty_str = ', '.join(str(ty) for ty in ret_tys)
self._emit_with_loc('\n{} = {}({}) : ({}) -> ({})'.format(
    ret_str, tfr_op_name, arg_str, arg_ty_str, ret_ty_str), node)
exit(list(zip(ret_ssa_values, ret_tys)))
