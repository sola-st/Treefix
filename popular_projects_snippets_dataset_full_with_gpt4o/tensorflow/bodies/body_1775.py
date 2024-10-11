# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
x = np.array([1., 2., 3.], dtype=np.float32)
y = np.array([11., 12., 13., 14.], dtype=np.float64)

def f(x, y):
    # (sin(x), cos(y))
    module = """
module @jit_f.0 {
  func.func public @main(%arg0: tensor<3xf32>, %arg1: tensor<4xf64>) -> (tensor<3xf32>, tensor<4xf64>) {
    %0 = stablehlo.sine %arg0 : tensor<3xf32>
    %1 = stablehlo.cosine %arg1 : tensor<4xf64>
    return %0, %1 : tensor<3xf32>, tensor<4xf64>
  }
}
"""
    exit(xla.call_module([x, y], version=2,
                           module=module,
                           Tout=[x.dtype, y.dtype],
                           Sout=[x.shape, y.shape]))

self._assertOpOutputMatchesExpected(f, (x, y), (np.sin(x), np.cos(y)))
