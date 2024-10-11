# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Remove redundant quantize ops per subgraph."""
subgraph = model.subgraphs[subgraph_index]
tensors = subgraph.tensors
operators = subgraph.operators

# Find all quantize operators.
quant_opcode_idxs = get_quantize_opcode_idx(model)
dequant_opcode_idxs = get_dequantize_opcode_idx(model)

# Find all redundant quant tensors.
all_quant_ops = []
redundant_quant_tensors = {}
output_dequant_tensors = {}
for op in operators:
    if op.opcodeIndex in quant_opcode_idxs:
        all_quant_ops.append(op)
        input_tensor = tensors[op.inputs[0]]
        output_tensor = tensors[op.outputs[0]]
        input_type = _convert_tflite_enum_type_to_tf_type(input_tensor.type)
        output_type = _convert_tflite_enum_type_to_tf_type(output_tensor.type)
        # This is a requantize op, so write down its input tensor index.
        if input_type != dtypes.float32 and output_type != dtypes.float32:
            redundant_quant_tensors[op.inputs[0]] = op
    if (op.opcodeIndex in dequant_opcode_idxs and
        op.outputs[0] in subgraph.outputs):
        output_dequant_tensors[op.inputs[0]] = op

  # Remove all the quant ops which produce the redundant quant tensors.
for op in all_quant_ops:
    output_tensor_idx = op.outputs[0]
    if output_tensor_idx in redundant_quant_tensors:
        requantize_op = redundant_quant_tensors[output_tensor_idx]
        if model.signatureDefs:
            signature_def = model.signatureDefs[0]
            for output in signature_def.outputs:
                if output.tensorIndex == op.outputs[0]:
                    output.tensorIndex = op.inputs[0]
      # Reset the input of the requantize op to the float input
        requantize_op.inputs[0] = op.inputs[0]
        operators.remove(op)

  # Remove all the quant ops which connect to the output dequant op.
for op in all_quant_ops:
    output_tensor_idx = op.outputs[0]
    if output_tensor_idx in output_dequant_tensors:
        dequant_op = output_dequant_tensors[output_tensor_idx]
        subgraph.outputs[subgraph.outputs == dequant_op.outputs[0]] = op.inputs[0]
        if signature_index >= 0:
            signature_def = model.signatureDefs[signature_index]
            for output in signature_def.outputs:
                if output.tensorIndex == dequant_op.outputs[0]:
                    output.tensorIndex = op.inputs[0]
        operators.remove(op)
        operators.remove(dequant_op)
