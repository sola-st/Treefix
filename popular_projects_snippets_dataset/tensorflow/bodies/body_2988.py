# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_binary_bcast_test.py
mlir_function = """
      func.func @compute(%arg0: tensor<*xf32> {rt.constraint = "rank"},
                         %arg1: tensor<f32>) -> tensor<*xf32> {
        %0 = "tf.AddV2"(%arg0, %arg1)
             : (tensor<*xf32>, tensor<f32>) -> tensor<*xf32>
        func.return %0 : tensor<*xf32>
      }"""

compiled = jitrt.compile(mlir_function, 'compute')

arg0 = np.random.uniform(0, 10.0, size=(4, 4)).astype(np.float32)
arg1 = np.random.uniform(0, 10.0, size=()).astype(np.float32)

[res] = jitrt.execute(compiled, [arg0, arg1])

np.testing.assert_allclose(res, np.add(arg0, arg1), atol=0.0)
