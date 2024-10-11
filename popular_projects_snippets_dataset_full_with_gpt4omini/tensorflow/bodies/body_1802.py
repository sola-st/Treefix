# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
module = """
module @jit_fun_3 {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<?xf32>) -> tensor<?xi32> {
    %0 = call @f(%arg0, %arg1) : (tensor<i32>, tensor<?xf32>) -> tensor<?xi32>
    return %0 : tensor<?xi32>
  }
  func.func private @f(%arg0: tensor<i32>, %arg1: tensor<?xf32>) -> tensor<?xi32> {
    %0 = stablehlo.reshape %arg0 : (tensor<i32>) -> tensor<1xi32>
    %1 = "stablehlo.dynamic_iota"(%0) {iota_dimension = 0 : i64} : (tensor<1xi32>) -> tensor<?xi32>
    return %1 : tensor<?xi32>
  }
}
"""
exit(xla.call_module([x,], version=2,
                       module=module,
                       Tout=[res.dtype],
                       Sout=[()],
                       dim_args_spec=['0.0']))
