# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_reduction_test.py
mlir_function = """
        func.func @test(%input: tensor<10xf32>) -> tensor<f32> {
          %dim_to_reduce =  "tf.Const"() {value = dense<[0]> : tensor<1xi32>}
             : () -> tensor<1xi32>
          %0 = "tf.Max"(%input, %dim_to_reduce) {keep_dims = false}
              : (tensor<10xf32>, tensor<1xi32>) -> tensor<f32>
          func.return %0 : tensor<f32>
      }"""

compiled = jitrt.compile(mlir_function, 'test', vectorize=True)

arg0 = np.random.uniform(1.0, 1.0, size=(10)).astype(np.float32)

[res] = jitrt.execute(compiled, [arg0])
np.testing.assert_allclose(res, np.max(arg0, axis=0), atol=0.01)
