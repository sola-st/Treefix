# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
# return x >= 1
module = """
module @jit_f_jax.0 {
  func.func public @main(%arg0: tensor<ui32>) -> tensor<i1> {
    %0 = stablehlo.constant dense<1> : tensor<ui32>
    %1 = "stablehlo.compare"(%arg0, %0) {compare_type = #stablehlo<comparison_type UNSIGNED>, comparison_direction = #stablehlo<comparison_direction GE>} : (tensor<ui32>, tensor<ui32>) -> tensor<i1>
    return %1 : tensor<i1>
  }
}
"""
exit(xla.call_module([x], version=2,
                       module=module,
                       Tout=[res.dtype],
                       Sout=[res.shape]))
