# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_reduction_test.py
mlir_function = """
        func.func @test(%input: tensor<8x8xf32>) -> tensor<8xf32> {
          %dim_to_reduce =  "tf.Const"() {value = dense<[1]> : tensor<1xi32>}
             : () -> tensor<1xi32>
          %0 = "tf.Sum"(%input, %dim_to_reduce) {keep_dims = false}
              : (tensor<8x8xf32>, tensor<1xi32>) -> tensor<8xf32>
          func.return %0 : tensor<8xf32>
      }"""

compiled = jitrt.compile(mlir_function, 'test', vectorize=True)

arg0 = np.random.uniform(0.0, 10.0, size=(8, 8)).astype(np.float32)

[res] = jitrt.execute(compiled, [arg0])
np.testing.assert_allclose(res, np.sum(arg0, axis=1), atol=1)
