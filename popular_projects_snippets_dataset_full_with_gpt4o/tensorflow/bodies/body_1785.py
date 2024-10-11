# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
x = np.ones((3, 5), dtype=np.int32)
res = np.arange(x.shape[0], dtype=np.int32)

def f(x):  # x: f32[b, 5]
    # return np.arange(x.shape[0], dtype=np.int32)
    module = """
module @jit_fun.1 {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<?x5xi32>) -> tensor<?xi32> {
    %0 = stablehlo.reshape %arg0 : (tensor<i32>) -> tensor<1xi32>
    %1 = "stablehlo.dynamic_iota"(%0) {iota_dimension = 0 : i64} : (tensor<1xi32>) -> tensor<?xi32>
    return %1 : tensor<?xi32>
  }
}
"""
    exit(xla.call_module([x,], version=2,
                           module=module,
                           Tout=[res.dtype],
                           Sout=[(None,)],
                           dim_args_spec=['0.0']))

self._assertOpOutputMatchesExpected(f, (x,), (res,))
