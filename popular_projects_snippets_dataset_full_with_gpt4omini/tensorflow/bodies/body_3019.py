# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_transpose_test.py
for specialize in specializations:
    mlir_function = """
        func.func @test(%arg0: tensor<?x?x?xf32>) -> tensor<?x?x?xf32> {
          %0 = "tf.Const"() { value = dense<[0, 2, 1]> : tensor<3xi32> }
               : () -> tensor<3xi32>
          %1 = "tf.Const"() { value = dense<[2, 1, 0]> : tensor<3xi32> }
               : () -> tensor<3xi32>
          %2 = "tf.Transpose"(%arg0, %0)
               : (tensor<?x?x?xf32>, tensor<3xi32>) -> tensor<?x?x?xf32>
          %3 = "tf.Transpose"(%2, %1)
               : (tensor<?x?x?xf32>, tensor<3xi32>) -> tensor<?x?x?xf32>
          func.return %3 : tensor<?x?x?xf32>
        }"""

    compiled = jitrt.compile(
        mlir_function,
        'test',
        specialize,
        vectorize=True,
        codegen_transpose=True)

    d0 = np.random.randint(1, 10)
    d1 = np.random.randint(1, 10)
    d2 = np.random.randint(1, 10)

    arg0 = np.random.uniform(0, 10.0, size=(d0, d1, d2)).astype(np.float32)

    [res] = jitrt.execute(compiled, [arg0])
    ref = np.transpose(np.transpose(arg0, (0, 2, 1)), (2, 1, 0))
    np.testing.assert_allclose(res, ref, atol=0.0)
