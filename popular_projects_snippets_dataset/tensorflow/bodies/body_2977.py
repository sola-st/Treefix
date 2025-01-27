# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_reduction_test.py
mlir_function = """
        func.func @test(%input: tensor<?x?xf32>) -> tensor<?xi64> {
          %dim_to_reduce = "tf.Const"() {value = dense<1> : tensor<i32>}
             : () -> tensor<i32>
          %0 = "tf.ArgMax"(%input, %dim_to_reduce)
              : (tensor<?x?xf32>, tensor<i32>) -> tensor<?xi64>
          func.return %0 : tensor<?xi64>
      }"""

compiled = jitrt.compile(mlir_function, 'test', vectorize=True)

arg0 = np.random.uniform(0.0, 10.0, size=(8, 10)).astype(np.float32)

[res] = jitrt.execute(compiled, [arg0])
np.testing.assert_equal(res, np.argmax(arg0, axis=1))
