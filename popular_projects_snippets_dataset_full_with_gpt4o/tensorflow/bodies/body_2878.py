# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
op_def, derived_attrs = self._op_defs.lookup(op_name)
ret_tys = [_get_type_from_proto(arg) for arg in op_def.output_arg]

ret_str, ret_ssa_values = self._get_mlir_ssa_values(op_name, ret_tys)

arg_strs = []
ty_strs = []
for arg in args:
    value, ty = self.visit(arg)
    arg_strs.append(value)
    ty_strs.append(str(ty))

input_args = [arg for arg in op_def.input_arg]
attrs_no_default = [
    attr for attr in op_def.attr
    if not attr.HasField('default_value') and attr.name not in derived_attrs
]
attrs_with_default = [
    attr for attr in op_def.attr
    if attr.HasField('default_value') and attr.name not in derived_attrs
]

kw_args = {}
for arg in keywords:
    value, (ssa_name, ty) = self.visit(arg)
    ty = self._get_inferred_type(arg.value, ty)

    # TODO(b/203493652): see comment on _ATTRIBUTE_RENAMES
    if op_name in _ATTRIBUTE_RENAMES and value in _ATTRIBUTE_RENAMES[op_name]:
        value = _ATTRIBUTE_RENAMES[op_name][value]

    kw_args[value] = (ssa_name, ty)

# tensor arguments and attribute arguments
ordered_args = input_args + attrs_no_default + attrs_with_default
for attr_def in ordered_args[len(args):]:
    if attr_def.name in kw_args:
        value, ty = kw_args[attr_def.name]
        if attr_def in input_args:
            if ty in _ATTRIBUTE_TYPES:
                # the argument shouldn't be used as tf op calls directly.
                value, ty = self._value_to_tensor(value, ty, node)
            if ty is TFRTypes.TENSOR_LIST and not _require_tensor_list(attr_def):
                value, ty = self._pack_tensor_list(value)
    else:
        value, ty = self._emit_default_constant_from_proto(attr_def)
    arg_strs.append(value)
    ty_strs.append(str(ty))

if ret_ssa_values:
    self.emit('\n{} = '.format(ret_str))

self.emit('tfr.call @tf__{}('.format(_camel_to_snake(op_name)))
arg_str = ', '.join(arg_strs)
arg_ty_str = ', '.join(ty_strs)
ret_ty_str = ', '.join([str(ty) for ty in ret_tys])
self._emit_with_loc(
    '{}) : ({}) -> ({})'.format(arg_str, arg_ty_str, ret_ty_str), node)
exit(list(zip(ret_ssa_values, ret_tys)))
