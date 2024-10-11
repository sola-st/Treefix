# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_reduction_test.py
mlir_function = """
        func.func @test(%input: tensor<?x?xf32>) -> tensor<?xf32> {
          %dim_to_reduce =  "tf.Const"() {value = dense<[0]> : tensor<1xi32>}
             : () -> tensor<1xi32>
          %0 = "tf.Sum"(%input, %dim_to_reduce) {keep_dims = false}
              : (tensor<?x?xf32>, tensor<1xi32>) -> tensor<?xf32>
          func.return %0 : tensor<?xf32>
      }"""

compiled = jitrt.compile(mlir_function, 'test', vectorize=True)

arg0 = np.random.uniform(0.0, 10.0, size=(8, 10)).astype(np.float32)

[res] = jitrt.execute(compiled, [arg0])
np.testing.assert_allclose(res, np.sum(arg0, axis=0), atol=0.01)
