# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/mlir/mlir_test.py

@def_function.function
def logging():
    logging_ops.print_v2('some message')

concrete_function = logging.get_concrete_function()
mlir_module = mlir.convert_function(concrete_function, pass_pipeline='')
self.assertRegex(mlir_module, r'tf\.PrintV2')
self.assertRegex(mlir_module, r'tf_executor.fetch.*: !tf_executor.control')
