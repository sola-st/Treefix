# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_softmax_test.py
mlir_function = """
        func.func @test(%input: tensor<10x8xf32>) -> tensor<10x8xf32> {
          %0 = "tf.Softmax"(%input) : (tensor<10x8xf32>) -> tensor<10x8xf32>
          func.return %0 : tensor<10x8xf32>
      }"""

compiled = jitrt.compile(mlir_function, 'test', vectorize=True)

arg0 = np.random.uniform(1, 5, size=(10, 8)).astype(np.float32)

[res] = jitrt.execute(compiled, [arg0])
np.testing.assert_allclose(res, softmax(arg0), atol=0.00001)
