# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
x = np.ones((4, 3), dtype=np.float32)
res = x.reshape((-1,))

def f(x):  # x: f32[b, 3]
    module = """
module @jit_fun_flat_jax {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<?x3xf32>) -> tensor<?xf32> {
    %0 = stablehlo.constant dense<3> : tensor<i32>
    %1 = stablehlo.multiply %arg0, %0 : tensor<i32>
    %2 = stablehlo.reshape %1 : (tensor<i32>) -> tensor<1xi32>
    %3 = stablehlo.dynamic_reshape %arg1, %2 : (tensor<?x3xf32>, tensor<1xi32>) -> tensor<?xf32>
    return %3 : tensor<?xf32>
  }
}
"""
    exit(xla.call_module([x],
                           module=module,
                           Tout=[res.dtype],
                           Sout=[(None,)],
                           dim_args_spec=['0.0']))

self._assertOpOutputMatchesExpected(f, (x,), (res,))
