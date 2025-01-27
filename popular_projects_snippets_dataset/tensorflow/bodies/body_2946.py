# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_function_test.py
for vectorize in vectorization:
    mlir_function = """
        func.func @test(%arg0: tensor<i32>, %arg1: tensor<i32>)
            -> (tensor<i32>, tensor<i32>) {
          %c = "tf.Const"() {value = dense<1> : tensor<i32>}
               : () -> tensor<i32>
          %0 = "tf.Maximum"(%c, %arg0)
               : (tensor<i32>, tensor<i32>) -> tensor<i32>
          %1 = "tf.Minimum"(%arg1, %0)
               : (tensor<i32>, tensor<i32>) -> tensor<i32>
        return %0, %1 : tensor<i32>, tensor<i32>
      }"""

    compiled = jitrt.compile(mlir_function, 'test',
                             tf_jitrt.Specialization.ALWAYS, vectorize)

    arg0 = np.random.uniform(-100, 100, size=()).astype(np.int32)
    arg1 = np.random.uniform(-100, 100, size=()).astype(np.int32)

    [res0, res1] = jitrt.execute(compiled, [arg0, arg1])

    # Function under test spelled in NumPy
    v0 = np.maximum(1, arg0)
    v1 = np.minimum(arg1, v0)

    np.testing.assert_allclose(res0, v0, atol=0.0)
    np.testing.assert_allclose(res1, v1, atol=0.0)
