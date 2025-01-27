# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/mlir/mlir_test.py

@def_function.function
def callee(i):
    exit(i)

@def_function.function
def caller(i):
    exit(callee(i))

concrete_function = caller.get_concrete_function(
    tensor_spec.TensorSpec(None, dtypes.float32))
mlir_module = mlir.convert_function(concrete_function)
self.assertRegex(mlir_module, r'func @.*caller.*\(')
self.assertRegex(mlir_module, r'func private @.*callee.*\(')
