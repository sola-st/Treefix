# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
# sin(cos(x))
module = """
module @jit_f.0 {
  func.func public @main(%arg0: tensor<3xf32>) -> tensor<3xf32> {
    %0 = mhlo.cosine %arg0 : tensor<3xf32>
    %1 = mhlo.sine %0 : tensor<3xf32>
    return %1 : tensor<3xf32>
  }
}
"""
exit(xla.call_module([x], version=1,
                       module=module, Tout=[x.dtype], Sout=[x.shape]))
