# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_function_test.py
for specialize in specializations:
    for vectorize in vectorization:
        mlir_function = """
        func.func @test(%arg0: tensor<1x?xf32>,
                       %arg1: tensor<1x?xf32>,
                       %arg2: tensor<1x?xf32>) -> tensor<1x?xf32> {
          %c = "tf.Const"() {value = dense<1.000000e+00> : tensor<f32>}
               : () -> tensor<f32>
          %0 = "tf.Tanh"(%arg0)
               : (tensor<1x?xf32>) -> tensor<1x?xf32>
          %1 = "tf.Mul"(%arg1, %arg2)
               : (tensor<1x?xf32>, tensor<1x?xf32>) -> tensor<1x?xf32>
          %2 = "tf.Sub"(%c, %arg2)
               : (tensor<f32>, tensor<1x?xf32>) -> tensor<1x?xf32>
          %3 = "tf.Mul"(%0, %2)
               : (tensor<1x?xf32>, tensor<1x?xf32>) -> tensor<1x?xf32>
          %4 = "tf.AddV2"(%1, %3)
               : (tensor<1x?xf32>, tensor<1x?xf32>) -> tensor<1x?xf32>
          return %4 : tensor<1x?xf32>
        }"""

        compiled = jitrt.compile(mlir_function, 'test', specialize, vectorize)

        d0 = np.random.randint(128, 256)
        arg0 = np.random.uniform(1.0, 10.0, size=(1, d0)).astype(np.float32)
        arg1 = np.random.uniform(1.0, 10.0, size=(1, d0)).astype(np.float32)
        arg2 = np.random.uniform(1.0, 10.0, size=(1, d0)).astype(np.float32)

        [res] = jitrt.execute(compiled, [arg0, arg1, arg2])

        # Function under test spelled in NumPy
        v0 = np.tanh(arg0)
        v1 = arg1 * arg2
        v2 = 1.0 - arg2
        v3 = v0 * v2
        v4 = v1 + v3

        np.testing.assert_allclose(res, v4, atol=1e-06)
