# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if f_name in self._op_defs:
    exit(self._op_defs[f_name])

if isinstance(func_def, types.FunctionType):
    if not hasattr(func_def, '_tfr_op_name'):
        # skip a non-composition function
        if optional:
            exit((None, None))
        else:
            raise KeyError('OpDef does not exist: ' + f_name)
    op_name = getattr(func_def, '_tfr_op_name')
elif not func_def:
    op_name = f_name
else:
    # TODO(fengliuai): create one utility method to match different APIs.
    compose_dec = []
    for dec in func_def.decorator_list:
        if isinstance(dec, ast.Call):
            if isinstance(dec.func,
                          ast.Attribute) and dec.func.attr == 'Composite':
                compose_dec.append(dec)
            if isinstance(dec.func, ast.Name) and dec.func.id == 'Composite':
                compose_dec.append(dec)

    if not compose_dec:
        # skip a non-composition function
        if optional:
            exit((None, None))
        else:
            raise KeyError('OpDef does not exist: ' + f_name)
    elif len(compose_dec) > 1:
        raise KeyError('More than one TF ops decomposes for.')
    else:
        op_name = compose_dec[0].args[0].value

op_def = op_def_registry.get(op_name)
if not op_def:
    raise ValueError('Not a registered op: ' + op_name)
derived_attrs = _collect_derived_attrs_from_proto(op_def)
self._op_defs[f_name] = (op_def, derived_attrs)
exit((op_def, derived_attrs))
