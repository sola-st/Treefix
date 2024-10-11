# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_function_test.py
for vectorize in vectorization:
    mlir_function = """
        func.func @test(%arg0: tensor<*xf32> {rt.constraint = "rank"},
                   %arg1: tensor<?x?xf32>,
                   %arg2: tensor<?x?xf32>,
                   %arg3: tensor<?x?xf32>) -> tensor<*xf32> {
          %0 = "tf.Mul"(%arg0, %arg1)
               : (tensor<*xf32>, tensor<?x?xf32>) -> tensor<*xf32>
          %1 = "tf.Mul"(%arg2, %arg3)
               : (tensor<?x?xf32>, tensor<?x?xf32>) -> tensor<?x?xf32>
          %2 = "tf.AddV2"(%0, %1)
               : (tensor<*xf32>, tensor<?x?xf32>) -> tensor<*xf32>
          return %2 : tensor<*xf32>
        }"""

    compiled = jitrt.compile(mlir_function, 'test',
                             tf_jitrt.Specialization.ALWAYS, vectorize)

    d0 = np.random.randint(4, 8)
    d1 = np.random.randint(4, 8)

    arg1 = np.random.uniform(1.0, 10.0, size=(d0, d1)).astype(np.float32)
    arg2 = np.random.uniform(1.0, 10.0, size=(d0, d1)).astype(np.float32)
    arg3 = np.random.uniform(1.0, 10.0, size=(d0, d1)).astype(np.float32)

    for shape in [(), (d1), (d0, d1)]:
        arg0 = np.random.uniform(1.0, 10.0, size=shape).astype(np.float32)
        [res] = jitrt.execute(compiled, [arg0, arg1, arg2, arg3])

        # Function under test spelled in NumPy
        v0 = arg0 * arg1
        v1 = arg2 * arg3
        v3 = v0 + v1

        np.testing.assert_allclose(res, v3, atol=0.0)
