# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_reduction_test.py
mlir_function = """
        func.func @test(%input: tensor<?x?xi1>) -> tensor<?xi1> {
          %dim_to_reduce =  "tf.Const"() {value = dense<[1]> : tensor<1xi32>}
             : () -> tensor<1xi32>
          %0 = "tf.Any"(%input, %dim_to_reduce) {keep_dims = false}
              : (tensor<?x?xi1>, tensor<1xi32>) -> tensor<?xi1>
          func.return %0 : tensor<?xi1>
      }"""

compiled = jitrt.compile(
    mlir_function, 'test', vectorize=True, legalize_i1_tensors=True)

arg0 = np.random.choice(a=[False, True], size=(8, 10)).astype(bool)

[res] = jitrt.execute(compiled, [arg0])
np.testing.assert_equal(res, np.any(arg0, axis=1))
