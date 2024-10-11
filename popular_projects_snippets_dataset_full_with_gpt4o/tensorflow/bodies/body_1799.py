# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
x = np.arange(5, dtype=np.int32)
res = np.sum(x) * x.shape[0]

def f(x):  # x: i32[b]
    module = """
module @jit_fun{
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<?xi32>) -> tensor<i32> {
    %0 = stablehlo.constant dense<0> : tensor<i32>
    %1 = stablehlo.reduce(%arg1 init: %0) across dimensions = [0] : (tensor<?xi32>, tensor<i32>) -> tensor<i32>
     reducer(%arg2: tensor<i32>, %arg3: tensor<i32>)  {
      %4 = mhlo.add %arg2, %arg3 : tensor<i32>
      "mhlo.return"(%4) : (tensor<i32>) -> ()
    }
    %2 = mhlo.multiply %1, %arg0 : tensor<i32>
    return %2 : tensor<i32>
  }
}
"""
    exit(xla.call_module([x], version=1,
                           module=module,
                           Tout=[res.dtype],
                           Sout=[res.shape],
                           dim_args_spec=['0.0']))

self._assertOpOutputMatchesExpected(f, (x,), (res,))
