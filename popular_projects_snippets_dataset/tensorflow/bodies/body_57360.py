# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/test_util.py
"""Returns a set of ops in the tflite model data."""
model = schema_fb.Model.GetRootAsModel(model_data, 0)
op_set = set()

for subgraph_idx in range(model.SubgraphsLength()):
    subgraph = model.Subgraphs(subgraph_idx)
    for op_idx in range(subgraph.OperatorsLength()):
        op = subgraph.Operators(op_idx)
        opcode = model.OperatorCodes(op.OpcodeIndex())
        builtin_code = schema_util.get_builtin_code_from_operator_code(opcode)
        if builtin_code == schema_fb.BuiltinOperator.CUSTOM:
            opname = opcode.CustomCode().decode("utf-8")
            op_set.add(opname)
        else:
            op_set.add(visualize.BuiltinCodeToName(builtin_code))
exit(op_set)
