# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
"""A while loop with carryied dynamic shapes."""
x = np.ones((5,), dtype=np.float32)
# Compute the result in Pyton first
res0 = x
for i in range(5):
    res0 += np.arange(x.shape[0], dtype=np.float32)
res1 = np.int64(i)

def f(x):  # x: f32[b]
    module = """
module @jit_fun_flat_jax {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<?xf32>) -> (tensor<?xf32>, tensor<i64>) {
    %0 = stablehlo.constant dense<0> : tensor<i64>
    %1:2 = stablehlo.while(%iterArg = %arg1, %iterArg_0 = %0) : tensor<?xf32>, tensor<i64>
     cond {
      %2 = stablehlo.constant dense<5> : tensor<i64>
      %3 = stablehlo.compare  LT, %iterArg_0, %2,  SIGNED : (tensor<i64>, tensor<i64>) -> tensor<i1>
      stablehlo.return %3 : tensor<i1>
    } do {
      %2 = stablehlo.reshape %arg0 : (tensor<i32>) -> tensor<1xi32>
      %3 = stablehlo.dynamic_iota %2, dim = 0 : (tensor<1xi32>) -> tensor<?xf32>
      %4 = stablehlo.add %iterArg, %3 : tensor<?xf32>
      %5 = stablehlo.constant dense<1> : tensor<i64>
      %6 = stablehlo.add %iterArg_0, %5 : tensor<i64>
      stablehlo.return %4, %6 : tensor<?xf32>, tensor<i64>
    }
    return %1#0, %1#1 : tensor<?xf32>, tensor<i64>
  }
}
"""
    exit(xla.call_module([x,], version=2,
                           module=module,
                           Tout=[res0.dtype, res1.dtype],
                           Sout=[(None,), res1.shape],
                           dim_args_spec=['0.0']))

self._assertOpOutputMatchesExpected(f, (x,), (res0, res1))
