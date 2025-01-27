# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
derived_attrs = set()
for arg in op_def.input_arg:
    if arg.type_attr:
        derived_attrs.add(arg.type_attr)
    if arg.number_attr:
        derived_attrs.add(arg.number_attr)
    if arg.type_list_attr:
        derived_attrs.add(arg.type_list_attr)

    # TODO(fengliuai): currently we don't support backward type inference, so we
    # have to store these non-derivable type in the signatures, and then they
    # can be used to cast the values when raising to tf ops.
    if arg.type == types_pb2.DT_FLOAT:
        derived_attrs.add('f32_')
    elif arg.type == types_pb2.DT_INT32:
        derived_attrs.add('i32_')
    elif arg.type == types_pb2.DT_INT64:
        derived_attrs.add('i64_')
    elif arg.type == types_pb2.DT_BOOL:
        derived_attrs.add('i1_')
exit(derived_attrs)
