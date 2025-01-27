# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_function_test.py
for vectorize in vectorization:
    mlir_function = """
        func.func @test(%arg0: tensor<*xf32> {rt.constraint = "rank"})
            -> (tensor<*xf32>, tensor<*xf32>) {
          %c = "tf.Const"() {value = dense<1.000000e+00> : tensor<f32>}
               : () -> tensor<f32>
          %0 = "tf.Sub"(%c, %arg0)
               : (tensor<f32>, tensor<*xf32>) -> tensor<*xf32>
          %1 = "tf.Sub"(%c, %0)
               : (tensor<f32>, tensor<*xf32>) -> tensor<*xf32>
          return %0, %1 : tensor<*xf32>, tensor<*xf32>
        }"""

    compiled = jitrt.compile(mlir_function, 'test',
                             tf_jitrt.Specialization.ALWAYS, vectorize)

    d0 = np.random.randint(128, 256)
    arg0 = np.random.uniform(1.0, 10.0, size=(1, d0)).astype(np.float32)

    [res0, res1] = jitrt.execute(compiled, [arg0])

    # Function under test spelled in NumPy
    v0 = 1.0 - arg0
    v1 = 1.0 - v0

    np.testing.assert_allclose(res0, v0, atol=0.0)
    np.testing.assert_allclose(res1, v1, atol=0.0)
