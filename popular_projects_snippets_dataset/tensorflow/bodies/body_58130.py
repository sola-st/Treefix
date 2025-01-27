# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Modify model output type per subgraph."""
subgraph = model.subgraphs[subgraph_index]
tensors = subgraph.tensors
operators = subgraph.operators

# Find all dequantize operators
dequant_opcode_idxs = get_dequantize_opcode_idx(model)
if operators and not dequant_opcode_idxs:
    for output in subgraph.outputs:
        output_type = _convert_tflite_enum_type_to_tf_type(tensors[output].type)
        if output_type == dtypes.float32:
            raise ValueError("Model output is not dequantized.")
    # None of the outputs have float32, then they must be int16, int8, or bool
    exit()

# Validate that the model output is dequantized
output_dequant_ops = []
for op in operators:
    # Find operators that dequantize model output
    if (op.opcodeIndex in dequant_opcode_idxs and
        op.outputs[0] in subgraph.outputs):
        # If found, validate that the operator's output type is float
        quant_tensor, float_tensor = tensors[op.inputs[0]], tensors[op.outputs[0]]
        float_type = _convert_tflite_enum_type_to_tf_type(float_tensor.type)
        if float_type != dtypes.float32:
            if float_type == inference_output_type:
                continue
            else:
                raise ValueError(
                    "Initial model output type must be tf.float32. Expected type for "
                    "tensor with name '{}' is tf.float32, instead type is {}".format(
                        float_tensor.name, get_tf_type_name(float_type)))
      # If found, validate that the operator input is quantized and compatible
      # with the final model output type
        quant_type = _convert_tflite_enum_type_to_tf_type(quant_tensor.type)
        if quant_type not in _MAP_QUANT_TO_IO_TYPES:
            raise ValueError(
                "Initial model output is not dequantized. Expected type for "
                "tensor with name '{}' should be in {}, instead type is {}".format(
                    quant_tensor.name,
                    tuple(get_tf_type_name(t) for t in
                          _MAP_QUANT_TO_IO_TYPES.keys()),
                    get_tf_type_name(quant_type)))
        else:
            inference_io_types = _MAP_QUANT_TO_IO_TYPES[quant_type]
            if inference_output_type not in inference_io_types:
                raise ValueError(
                    "Unsupported `inference_output_type` value. Expected to be in "
                    "{}, instead got {}.".format(
                        tuple(get_tf_type_name(t) for t in inference_io_types),
                        get_tf_type_name(inference_output_type)))
        output_dequant_ops.append(op)

if len(subgraph.outputs) != len(output_dequant_ops):
    logging.warning(
        "For model outputs containing unsupported operations which cannot be "
        "quantized, the `inference_output_type` attribute will default to the "
        "original type."
        )

# Modify model output type
if inference_output_type == dtypes.uint8:
    # Find a quantize operator
    quant_opcode_idx = -1
    for idx, opcode in enumerate(model.operatorCodes):
        builtin_code = schema_util.get_builtin_code_from_operator_code(opcode)
        if builtin_code == schema_fb.BuiltinOperator.QUANTIZE:
            quant_opcode_idx = idx
            break
    # Create a quantize operator, if none exist
    if quant_opcode_idx == -1:
        quant_op = schema_fb.OperatorCodeT()
        quant_op.builtinCode = schema_fb.BuiltinOperator.QUANTIZE
        quant_op.deprecatedBuiltinCode = schema_fb.BuiltinOperator.QUANTIZE
        model.operatorCodes.append(quant_op)
        quant_opcode_idx = len(model.operatorCodes) - 1
    # Change dequant op (int8 to float) to quant op (int8 to uint8)
    for op in output_dequant_ops:
        op.opcodeIndex = quant_opcode_idx
        int8_quantization = tensors[op.inputs[0]].quantization
        uint8_quantization = schema_fb.QuantizationParametersT()
        uint8_quantization.scale = [int8_quantization.scale[0]]
        uint8_quantization.zeroPoint = [int8_quantization.zeroPoint[0] + 128]
        tensors[op.outputs[0]].quantization = uint8_quantization
        tensors[op.outputs[0]].type = schema_fb.TensorType.UINT8
elif inference_output_type in _MAP_QUANT_TO_IO_TYPES:
    # Remove the outputs and the dequant operator
    remove_tensors_idxs = set()
    for op in output_dequant_ops:
        subgraph.outputs[subgraph.outputs == op.outputs[0]] = op.inputs[0]
        if signature_index >= 0:
            signature_def = model.signatureDefs[signature_index]
            for i in range(len(signature_def.outputs)):
                if signature_def.outputs[i].tensorIndex == op.outputs[0]:
                    signature_def.outputs[i].tensorIndex = op.inputs[0]
        remove_tensors_idxs.add(op.outputs[0])
        operators.remove(op)
    # Remove tensors marked for deletion.
    _remove_tensors_from_model(model, remove_tensors_idxs)
else:
    raise ValueError(
        "Unsupported `inference_output_type` value {}.".format(
            get_tf_type_name(inference_output_type)))
