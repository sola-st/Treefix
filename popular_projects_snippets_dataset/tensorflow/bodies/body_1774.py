# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
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
