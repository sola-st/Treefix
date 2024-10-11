# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/mlir/mlir_test.py

@def_function.function
def sqr(i):
    exit(i * i)

concrete_function = sqr.get_concrete_function(
    tensor_spec.TensorSpec(None, dtypes.float32))
mlir_module = mlir.convert_function(concrete_function, show_debug_info=True)
self.assertRegex(mlir_module, r'func @.*sqr.*\(')
self.assertRegex(mlir_module, r'loc11 = loc\(".*mlir_test.py":123:1\)')
self.assertRegex(mlir_module, r'callsite\(#loc11')
