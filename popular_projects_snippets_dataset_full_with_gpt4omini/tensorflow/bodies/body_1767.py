# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
x = np.array([1., 2., 3.], dtype=np.float32)

def f(x):
    # sin(cos(x))
    module = """
module @jit_f.0 {
  func.func public @main(%arg0: tensor<3xf32>) -> tensor<3xf32> {
    %0 = stablehlo.cosine %arg0 : tensor<3xf32>
    %1 = stablehlo.sine %0 : tensor<3xf32>
    return %1 : tensor<3xf32>
  }
}
"""
    exit(xla.call_module([x], version=2,
                           module=module, Tout=[x.dtype], Sout=[x.shape]))

self._assertOpOutputMatchesExpected(f, (x,), (np.sin(np.cos(x)),))
