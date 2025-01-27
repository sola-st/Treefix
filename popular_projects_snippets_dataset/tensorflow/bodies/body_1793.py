# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
x = np.ones((3, 4), dtype=np.float32)
res = x[-1, :]  # TODO(necula): adjust this, if not the right result

def f(x):  # x: f32[b, 4]
    module = """
module @jit_fun_flat_jax {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<?x4xf32>) -> tensor<4xf32> {
    %0 = stablehlo.constant dense<-1> : tensor<i32>
    %1 = stablehlo.add %arg0, %0 : tensor<i32>
    %2 = stablehlo.reshape %1 : (tensor<i32>) -> tensor<1xi32>
    %3 = stablehlo.constant dense<0> : tensor<1xi32>
    %4 = stablehlo.concatenate %2, %3, dim = 0 : (tensor<1xi32>, tensor<1xi32>) -> tensor<2xi32>
    %5 = stablehlo.reshape %arg0 : (tensor<i32>) -> tensor<1xi32>
    %6 = stablehlo.constant dense<4> : tensor<1xi32>
    %7 = stablehlo.concatenate %5, %6, dim = 0 : (tensor<1xi32>, tensor<1xi32>) -> tensor<2xi32>
    %10 = stablehlo.constant dense<1> : tensor<2xi32>
    %11 = stablehlo.real_dynamic_slice %arg1, %4, %7, %10 : (tensor<?x4xf32>, tensor<2xi32>, tensor<2xi32>, tensor<2xi32>) -> tensor<1x4xf32>
    %12 = stablehlo.reshape %11 : (tensor<1x4xf32>) -> tensor<4xf32>
    return %12 : tensor<4xf32>
  }
}
"""
    exit(xla.call_module([x],
                           module=module,
                           Tout=[x.dtype],
                           Sout=[(4,)],
                           dim_args_spec=['0.0']))

self._assertOpOutputMatchesExpected(f, (x,), (res,))
