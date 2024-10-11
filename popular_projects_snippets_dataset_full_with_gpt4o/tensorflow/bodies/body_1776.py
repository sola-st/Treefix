# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
# Module takes another argument which is the value of b
# (sin(x), x.shape[1])
module = """
module @jit_f.0 {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<2x?xf32>) -> (tensor<2x?xf32>, tensor<i32>) {
    %0 = stablehlo.sine %arg1 : tensor<2x?xf32>
    return %0, %arg0 : tensor<2x?xf32>, tensor<i32>
  }
}
"""
exit(xla.call_module([x],
                       version=2,
                       module=module,
                       Tout=[x.dtype, np.int32],
                       Sout=[(None, 3), ()],
                       dim_args_spec=['0.1']))
