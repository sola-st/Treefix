# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_const_test.py
mlir_function = """
      func.func @test() -> tensor<2xi32> {
        %0 = "tf.Const"() {value = dense<0> : tensor<i32>} : () -> tensor<i32>
        %1 = "tf.Const"() {value = dense<1> : tensor<i32>} : () -> tensor<i32>
        %2 = "tf.Pack"(%0, %1) {axis = 0 : i64}
             : (tensor<i32>, tensor<i32>) -> tensor<2xi32>
        func.return %2 : tensor<2xi32>
      }"""

compiled = jitrt.compile(mlir_function, 'test')
[res] = jitrt.execute(compiled, [])
np.testing.assert_allclose(res, [0, 1], rtol=0.0)
