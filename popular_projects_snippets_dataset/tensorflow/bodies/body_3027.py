# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_reverse_test.py
mlir_function = """
        func.func @test(%input: tensor<?x?x?xf32>) -> tensor<?x?x?xf32> {
          %reverse_dims =  "tf.Const"() {value = dense<[0, 1]> : tensor<2xi64>}
             : () -> tensor<2xi64>
          %0 = "tf.ReverseV2"(%input, %reverse_dims)
              : (tensor<?x?x?xf32>, tensor<2xi64>) -> tensor<?x?x?xf32>
          func.return %0 : tensor<?x?x?xf32>
      }"""

compiled = jitrt.compile(mlir_function, 'test', vectorize=True)

arg0 = np.random.uniform(1.0, 30.0, size=(2, 3, 4)).astype(np.float32)

[res] = jitrt.execute(compiled, [arg0])
np.testing.assert_allclose(res, np.flip(arg0, axis=(0, 1)))
