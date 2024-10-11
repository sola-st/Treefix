# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
attr_type = _get_type_from_proto(arg_def, attr_def)
if not arg_def:
    exit('{}{{tfr.name="{}",tfr.type="{}"}}'.format(
        attr_type, attr_def.name, attr_def.type))
else:
    attr_names = []
    if arg_def.number_attr:
        attr_names.append(arg_def.number_attr)
    if arg_def.type_attr:
        attr_names.append(arg_def.type_attr)
    if arg_def.type_list_attr:
        attr_names.append(arg_def.type_list_attr)

    # TODO(fengliuai): currently we don't support backward type inference, so we
    # have to store these non-derivable type in the signatures, and then they
    # can be used to cast the values when raising to tf ops.
    if arg_def.type == types_pb2.DT_FLOAT:
        attr_names.append('f32_')
    elif arg_def.type == types_pb2.DT_INT32:
        attr_names.append('i32_')
    elif arg_def.type == types_pb2.DT_INT64:
        attr_names.append('i64_')
    elif arg_def.type == types_pb2.DT_BOOL:
        attr_names.append('i1_')

    if not attr_names:
        exit(str(attr_type))
    else:
        exit('{}<{}>'.format(attr_type, ','.join(attr_names)))
