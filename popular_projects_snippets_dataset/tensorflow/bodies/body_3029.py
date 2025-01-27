# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_select_test.py
for specialize in specializations:
    mlir_function = """
        func.func @test(%arg0: tensor<?xf32>)
               -> (tensor<?xf32>, tensor<?xi1>, tensor<?xf32>)
        {
          %c = "tf.Const"() {value = dense<0.0> : tensor<f32>}
               : () -> tensor<f32>
          %0 = "tf.ZerosLike"(%arg0)
               : (tensor<?xf32>) -> tensor<?xf32>
          %1 = "tf.Less"(%arg0, %c)
               : (tensor<?xf32>, tensor<f32>) -> tensor<?xi1>
          %2 = "tf.Select"(%1, %0, %arg0)
               : (tensor<?xi1>, tensor<?xf32>, tensor<?xf32>) -> tensor<?xf32>
          func.return %0, %1, %2 : tensor<?xf32>, tensor<?xi1>, tensor<?xf32>
        }"""

    compiled = jitrt.compile(mlir_function, 'test', specialize)

    d0 = np.random.randint(1, 10)
    arg0 = np.random.uniform(0, 10.0, size=(d0)).astype(np.float32)

    [zeros, less, res] = jitrt.execute(compiled, [arg0])
    np.testing.assert_allclose(zeros, np.zeros_like(arg0), atol=0.0)
    np.testing.assert_allclose(less, np.less(arg0, 0.0), atol=0.0)
    np.testing.assert_allclose(res, np.clip(arg0, 0.0, None), atol=0.0)
