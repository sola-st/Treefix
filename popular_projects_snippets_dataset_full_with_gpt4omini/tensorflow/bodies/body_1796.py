# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
# return (np.broadcast_to(x, y.shape), x + y)
module = """
module @jit_fun.0 {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<?x4xf32>, %arg2: tensor<2x?x4xf32>) -> (tensor<2x?x4xf32>, tensor<2x?x4xf32>) {
    %0 = stablehlo.constant dense<2> : tensor<1xi32>
    %2 = stablehlo.reshape %arg0 : (tensor<i32>) -> tensor<1xi32>
    %3 = stablehlo.constant dense<4> : tensor<1xi32>
    %4 = "stablehlo.concatenate"(%0, %2, %3) {dimension = 0 : i64} : (tensor<1xi32>, tensor<1xi32>, tensor<1xi32>) -> tensor<3xi32>
    %5 = "stablehlo.dynamic_broadcast_in_dim"(%arg1, %4) {broadcast_dimensions = dense<[1, 2]> : tensor<2xi64>} : (tensor<?x4xf32>, tensor<3xi32>) -> tensor<2x?x4xf32>
    %6 = stablehlo.add %5, %arg2 : (tensor<2x?x4xf32>, tensor<2x?x4xf32>) -> tensor<2x?x4xf32>
    return %5, %6 : tensor<2x?x4xf32>, tensor<2x?x4xf32>
  }
}
"""
exit(xla.call_module([x, y], version=2,
                       module=module,
                       Tout=[res[0].dtype, res[1].dtype],
                       Sout=[(2, None, 4), (2, None, 4)],
                       dim_args_spec=['1.1']))
