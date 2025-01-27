# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/multiple_results_test.py
for specialize in specializations:
    mlir_function = """
        func.func @test(%arg0: tensor<?xf32>) -> (tensor<?xf32>, tensor<?xf32>) {
          %0 = "tf.Const"() { value = dense<1.0> : tensor<f32> }
               : () -> tensor<f32>
          %1 = "tf.AddV2"(%arg0, %0)
               : (tensor<?xf32>, tensor<f32>) -> tensor<?xf32>
          %2 = "tf.AddV2"(%1, %0)
               : (tensor<?xf32>, tensor<f32>) -> tensor<?xf32>
          func.return %1, %2 : tensor<?xf32>, tensor<?xf32>
        }"""

    compiled = jitrt.compile(mlir_function, 'test', specialize)

    d0 = np.random.randint(1, 10)
    arg0 = np.zeros(d0, np.float32)

    [res0, res1] = jitrt.execute(compiled, [arg0])
    np.testing.assert_allclose(res0, arg0 + 1.0, atol=0.0)
    np.testing.assert_allclose(res1, arg0 + 2.0, atol=0.0)
