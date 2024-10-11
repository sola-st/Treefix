# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
tfr_funcs = set()
for _, (op_def, derived_attrs) in sorted(self._op_defs.items()):
    tfr_func = '\ntfr.func @tf__{}_('.format(_camel_to_snake(op_def.name))

    # tensor inputs
    inputs = [
        _get_type_info_from_proto(arg_def) for arg_def in op_def.input_arg
    ]

    # attribute inputs. The attribute with default values are moved backwards.
    non_derived_attrs = [
        attr for attr in op_def.attr if attr.name not in derived_attrs
    ]
    attrs_no_default = [
        attr for attr in non_derived_attrs
        if not attr.HasField('default_value')
    ]
    attrs_with_default = [
        attr for attr in non_derived_attrs if attr.HasField('default_value')
    ]
    attr_names = {'f32_', 'i32_', 'i64_', 'i1_'}  # reserved
    for attr_def in attrs_no_default + attrs_with_default:
        inputs.append(_get_type_info_from_proto(None, attr_def))
        attr_names.add(attr_def.name)

    # tensor outputs
    outputs = [
        _get_type_info_from_proto(arg_def) for arg_def in op_def.output_arg
    ]

    inputs = ','.join(inputs)
    outputs = ','.join(outputs)
    attrs = ','.join(sorted(derived_attrs.union(attr_names)))
    tfr_funcs.add('{}{}) -> ({}) attributes {{{}}}'.format(
        tfr_func, inputs, outputs, attrs))
exit(sorted(list(tfr_funcs)))
