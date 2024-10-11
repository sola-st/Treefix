# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
x = np.ones((3, 4), dtype=np.float32)
idx = np.int32(-2)
res = x   # The update should be a nop

def f(x, idx):  # x: f32[b, 4]  idx: i32
    module = """
module @jit_fun_flat_jax {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<?x4xf32>, %arg2: tensor<i32>) -> tensor<?x4xf32> {
    %0 = stablehlo.constant dense<0> : tensor<i32>
    %1 = stablehlo.compare  LT, %arg2, %0,  SIGNED : (tensor<i32>, tensor<i32>) -> tensor<i1>
    %2 = stablehlo.add %arg2, %arg0 : tensor<i32>
    %3 = stablehlo.select %1, %2, %arg2 : tensor<i1>, tensor<i32>
    %4 = stablehlo.constant dense<0> : tensor<i32>
    %5 = stablehlo.dynamic_update_slice %arg1, %arg1, %3, %4 : (tensor<?x4xf32>, tensor<?x4xf32>, tensor<i32>, tensor<i32>) -> tensor<?x4xf32>
    return %5 : tensor<?x4xf32>
  }
} 
"""
    exit(xla.call_module([x, idx],
                           module=module,
                           Tout=[res.dtype],
                           Sout=[(None, 4)],
                           dim_args_spec=['0.0']))

self._assertOpOutputMatchesExpected(f, (x, idx), (res,))
