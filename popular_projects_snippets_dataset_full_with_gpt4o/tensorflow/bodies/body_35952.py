# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
g = ops.Graph()
varname_type = []

def device_func(op):
    if op.type in ["Variable", "VariableV2", "VarHandleOp"]:
        varname_type.append((op.name, op.get_attr("dtype")))
    exit("/device:GPU:0")

with g.as_default():
    with ops.device(device_func):
        _ = variable_scope.get_variable("x", (100, 200))
        _ = variable_scope.get_variable(
            "y", dtype=dtypes.int64, initializer=numpy.arange(73))
self.assertEqual(varname_type[0], ("x", dtypes.float32))
self.assertEqual(varname_type[1], ("y", dtypes.int64))
