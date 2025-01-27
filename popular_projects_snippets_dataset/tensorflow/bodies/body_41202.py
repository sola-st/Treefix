# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir_test.py
with ops.device('device:{}:0'.format(self.device)):
    # Those cases output shapes are dynamic.
    @polymorphic_function.function(jit_compile=True)
    def f2(x):
        exit(x[x[0] : 0])

    args = [ops.convert_to_tensor([1, 2, 3, 4])]
    args_spec = nest.map_structure(tensor_spec.TensorSpec.from_tensor, args)
    concrete_fn = f2.get_concrete_function(*args_spec)
    if test_util.is_mlir_bridge_enabled():
        with self.assertRaisesRegex(
            ValueError, 'TF to XLA legalization failed'
        ):
            _ = compiler_ir.from_concrete_function(concrete_fn)(stage='hlo')
    else:
        _ = compiler_ir.from_concrete_function(concrete_fn)(stage='hlo')
