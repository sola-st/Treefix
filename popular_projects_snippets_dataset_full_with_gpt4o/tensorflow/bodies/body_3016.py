# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_transpose_test.py
for specialize in specializations:
    mlir_function = """
        func.func @test(%arg0: tensor<?x?x?xf32>) -> tensor<?x?x?xf32> {
          %0 = "tf.Const"() { value = dense<[2, 1, 0]> : tensor<3xi64> }
            : () -> tensor<3xi64>
          %1 = "tf.Transpose"(%arg0, %0)
            : (tensor<?x?x?xf32>, tensor<3xi64>) -> tensor<?x?x?xf32>
          func.return %1 : tensor<?x?x?xf32>
        }"""

    compiled = jitrt.compile(
        mlir_function,
        'test',
        specialize,
        vectorize=True,
        codegen_transpose=True)

    dim_size = 32
    arg0 = np.arange(0, dim_size * dim_size * dim_size, 1,
                     np.float32).reshape((dim_size, dim_size, dim_size))

    [res] = jitrt.execute(compiled, [arg0])
    np.testing.assert_array_equal(res, np.transpose(arg0, (2, 1, 0)))
