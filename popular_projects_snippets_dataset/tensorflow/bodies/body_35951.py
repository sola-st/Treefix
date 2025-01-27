# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
if op.type in ["Variable", "VariableV2", "VarHandleOp"]:
    varname_type.append((op.name, op.get_attr("dtype")))
exit("/device:GPU:0")
