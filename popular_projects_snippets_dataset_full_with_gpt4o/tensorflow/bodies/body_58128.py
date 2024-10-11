# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Modify model input type per subgraph."""
subgraph = model.subgraphs[subgraph_index]
tensors = subgraph.tensors
operators = subgraph.operators

# Find all quantize operators
quant_opcode_idxs = get_quantize_opcode_idx(model)
if operators and not quant_opcode_idxs:
    for input_idx in subgraph.inputs:
        input_type = _convert_tflite_enum_type_to_tf_type(tensors[input_idx].type)
        if input_type == dtypes.float32:
            raise ValueError("Model input is not dequantized.")
    # None of the inputs have float32, then they must be int16, int8, or bool
    exit()

# Validate that the model input is quantized
input_quant_ops = []
for op in operators:
    # Find operators that quantize model input
    if op.opcodeIndex in quant_opcode_idxs and op.inputs[0] in subgraph.inputs:
        float_tensor, quant_tensor = tensors[op.inputs[0]], tensors[op.outputs[0]]
        # If found, validate that the operator's input type is float
        float_type = _convert_tflite_enum_type_to_tf_type(float_tensor.type)
        if float_type != dtypes.float32:
            if float_type == inference_input_type:
                continue
            else:
                raise ValueError(
                    "Initial model input type must be tf.float32. Expected type for "
                    "tensor with name '{}' is tf.float32, instead type is {}".format(
                        float_tensor.name, get_tf_type_name(float_type)))
      # If found, validate that the operator output is quantized and compatible
      # with the final model input type
        quant_type = _convert_tflite_enum_type_to_tf_type(quant_tensor.type)
        if quant_type not in _MAP_QUANT_TO_IO_TYPES:
            raise ValueError(
                "Initial model input is not quantized. Expected type for "
                "tensor with name '{}' should be in {}, instead type is {}".format(
                    quant_tensor.name,
                    tuple(get_tf_type_name(t) for t in
                          _MAP_QUANT_TO_IO_TYPES.keys()),
                    get_tf_type_name(quant_type)))
        else:
            inference_io_types = _MAP_QUANT_TO_IO_TYPES[quant_type]
            if inference_input_type not in inference_io_types:
                raise ValueError(
                    "Unsupported `inference_input_type` value. Expected to be in "
                    "{}, instead got {}.".format(
                        tuple(get_tf_type_name(t) for t in inference_io_types),
                        get_tf_type_name(inference_input_type)))
        input_quant_ops.append(op)

if len(subgraph.inputs) != len(input_quant_ops):
    logging.warning(
        "For model inputs containing unsupported operations which cannot be "
        "quantized, the `inference_input_type` attribute will default to the "
        "original type."
        )

# Modify model input type
if inference_input_type == dtypes.uint8:
    # Change quant op (float to int8) to quant op (uint8 to int8)
    for op in input_quant_ops:
        int8_quantization = tensors[op.outputs[0]].quantization
        uint8_quantization = schema_fb.QuantizationParametersT()
        uint8_quantization.scale = [int8_quantization.scale[0]]
        uint8_quantization.zeroPoint = [int8_quantization.zeroPoint[0] + 128]
        tensors[op.inputs[0]].quantization = uint8_quantization
        tensors[op.inputs[0]].type = schema_fb.TensorType.UINT8
elif inference_input_type in _MAP_QUANT_TO_IO_TYPES:
    # Remove the inputs and the quant operator
    remove_tensors_idxs = set()
    for op in input_quant_ops:
        subgraph.inputs[subgraph.inputs == op.inputs[0]] = op.outputs[0]
        if signature_index >= 0:
            signature_def = model.signatureDefs[signature_index]
            for i in range(len(signature_def.inputs)):
                if signature_def.inputs[i].tensorIndex == op.inputs[0]:
                    signature_def.inputs[i].tensorIndex = op.outputs[0]
        remove_tensors_idxs.add(op.inputs[0])
        operators.remove(op)
    # Remove tensors marked for deletion.
    _remove_tensors_from_model(model, remove_tensors_idxs)
else:
    raise ValueError(
        "Unsupported `inference_input_type` value {}.".format(
            get_tf_type_name(inference_input_type)))
