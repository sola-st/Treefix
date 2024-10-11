# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
x = np.ones((5,), dtype=np.float32)
res = x

def f(x):  # x: f32[b]
    module = """
module @jit_fun_3 {
  func.func public @main(%arg0: tensor<i32>, %arg1: tensor<?xf32>) -> tensor<?xf32> {
    return %arg1 : tensor<?xf32>
  }
}
"""
    exit(xla.call_module([x],
                           version=2,
                           module=module,
                           Tout=[res.dtype],
                           Sout=[()],
                           dim_args_spec=['0.0']))

self._assertOpOutputMatchesExpected(f, (x,), (res,))
