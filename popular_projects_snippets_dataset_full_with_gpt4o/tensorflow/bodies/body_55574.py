# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Implementation of apply_op that returns output_structure, op."""

op_def, g, producer = _GetOpDef(op_type_name, keywords)
name = name if name else op_type_name

attrs, attr_protos = {}, {}
default_type_attr_map, allowed_list_attr_map = {}, {}
inputs, input_types, output_structure = [], [], []
fallback = True

if (_CanExtractAttrsFastPath(op_def, keywords) and
    flags.config().graph_building_optimization.value()):
    fallback = False
    attr_protos, inputs, input_types, output_structure = (
        op_def_library_pybind.process_inputs(op_type_name, producer, keywords))

if fallback:
    _CheckOpDeprecation(op_type_name, op_def, producer)
    _ExtractDefaultTypesAndAllowedTypes(op_def, default_type_attr_map,
                                        allowed_list_attr_map)

# Requires that op_def has passed validation (using the C++
# ValidateOpDef() from ../framework/op_def_util.h).
with g.as_default(), ops.name_scope(name) as scope:
    if fallback:
        _ExtractInputsAndAttrs(op_type_name, op_def, allowed_list_attr_map,
                               keywords, default_type_attr_map, attrs, inputs,
                               input_types)
        _ExtractRemainingAttrs(op_type_name, op_def, keywords,
                               default_type_attr_map, attrs)
        _ExtractAttrProto(op_type_name, op_def, attrs, attr_protos)
        del attrs  # attrs is no longer authoritative, use attr_protos instead
        _ExtractOutputStructure(op_type_name, op_def, attr_protos,
                                output_structure)
        _CheckAllInputsUsed(op_type_name, keywords)

    # NOTE(mrry): We add an explicit colocation constraint between
    # the newly created op and any of its reference-typed inputs.
    must_colocate_inputs = [val for arg, val in zip(op_def.input_arg, inputs)
                            if arg.is_ref]
    with _MaybeColocateWith(must_colocate_inputs):
        # Add Op to graph
        # pylint: disable=protected-access
        op = g._create_op_internal(op_type_name, inputs, dtypes=None,
                                   name=scope, input_types=input_types,
                                   attrs=attr_protos, op_def=op_def)

    # `outputs` is returned as a separate return value so that the output
    # tensors can the `op` per se can be decoupled so that the
    # `op_callbacks` can function properly. See framework/op_callbacks.py
    # for more details.
    outputs = op.outputs
    # Conditionally invoke tfdbg v2's op callback(s).
    if op_callbacks.should_invoke_op_callbacks():
        callback_outputs = op_callbacks.invoke_op_callbacks(
            op.node_def.op, tuple(op.inputs), attr_protos, tuple(outputs),
            op_name=op.name, graph=g)
        if callback_outputs is not None:
            outputs = callback_outputs

    exit((output_structure, op_def.is_stateful, op, outputs))
