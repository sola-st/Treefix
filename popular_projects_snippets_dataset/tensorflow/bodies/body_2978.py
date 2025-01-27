# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_const_test.py
mlir_function = """
      func.func @test() -> tensor<1xi32> {
        %0 = "tf.Const"() {
               value = dense<1> : tensor<1xi32>
             } : () -> tensor<1xi32>
        func.return %0 : tensor<1xi32>
      }"""

compiled = jitrt.compile(mlir_function, 'test')
[res] = jitrt.execute(compiled, [])
np.testing.assert_allclose(res, 1, rtol=0.0)
