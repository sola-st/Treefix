# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
x = np.ones((4, 2, 3), dtype=np.float32)
res = np.sin(x).reshape((4, -1))

def f(x):  # x: f32[b, 2, 3]
    module = """
module @jit_fun_flat_jax {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<?x2x3xf32>) -> tensor<?x6xf32> {
    %0 = stablehlo.sine %arg1 : tensor<?x2x3xf32>
    %1 = stablehlo.reshape %arg0 : (tensor<i32>) -> tensor<1xi32>
    %2 = stablehlo.constant dense<6> : tensor<1xi32>
    %3 = stablehlo.concatenate %1, %2, dim = 0 : (tensor<1xi32>, tensor<1xi32>) -> tensor<2xi32>
    %4 = stablehlo.dynamic_reshape %0, %3 : (tensor<?x2x3xf32>, tensor<2xi32>) -> tensor<?x6xf32>
    return %4 : tensor<?x6xf32>
  }
}
"""
    exit(xla.call_module([x],
                           module=module,
                           Tout=[res.dtype],
                           Sout=[(None, 6)],
                           dim_args_spec=['0.0']))

self._assertOpOutputMatchesExpected(f, (x,), (res,))
