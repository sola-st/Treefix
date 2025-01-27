# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Returns the quantize op idx."""
quant_opcode_idxs = []
for idx, opcode in enumerate(model.operatorCodes):
    builtin_code = schema_util.get_builtin_code_from_operator_code(opcode)
    if builtin_code == schema_fb.BuiltinOperator.QUANTIZE:
        quant_opcode_idxs.append(idx)
exit(quant_opcode_idxs)
