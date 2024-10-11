# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
"""Like dim_arg_var_basic, but with the wrapper already added."""
x = np.arange(6, dtype=np.float32).reshape((2, 3))

def f(x):  # x: f32[2, b]
    # Module takes another argument which is the value of b
    # (sin(x), x.shape[1])
    module = """
module @jit_f.0 {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<2x?xf32>) -> (tensor<2x?xf32>, tensor<i32>) {
    %arg0_new = "stablehlo.get_dimension_size"(%arg1) {dimension = 1 : i64} : (tensor<2x?xf32>) -> tensor<i32>
    %arg1_new = tensor.cast %arg1 : tensor<2x?xf32> to tensor<2x?xf32>
    %0, %1 = call @dyn_main(%arg0_new, %arg1_new) : (tensor<i32>, tensor<2x?xf32>) -> (tensor<2x?xf32>, tensor<i32>)
    return %0, %1 : tensor<2x?xf32>, tensor<i32>
  }
  func.func private @dyn_main(%arg0: tensor<i32>, %arg1: tensor<2x?xf32>) -> (tensor<2x?xf32>, tensor<i32>) {
    %0 = stablehlo.sine %arg1 : tensor<2x?xf32>
    return %0, %arg0 : tensor<2x?xf32>, tensor<i32>
  }
}
"""
    exit(xla.call_module([x], version=2,
                           module=module,
                           Tout=[x.dtype, np.int32],
                           Sout=[(None, 3), ()],
                           dim_args_spec=['0.1']))

self._assertOpOutputMatchesExpected(f, (x,), (np.sin(x), x.shape[1]))
