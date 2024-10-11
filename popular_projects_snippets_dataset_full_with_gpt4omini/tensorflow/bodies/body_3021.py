# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_transpose_test.py
mlir_function = """
      func.func @compute(%arg0: tensor<*xf32>,
                    %arg1: tensor<?xi64> {rt.constraint = "value"},
                    %arg2: tensor<?xi64> {rt.constraint = "value"})
          -> tensor<*xf32> {
        %0 = "tf.Transpose"(%arg0, %arg1)
             : (tensor<*xf32>, tensor<?xi64>) -> tensor<*xf32>
        %1 = "tf.Transpose"(%0, %arg2)
             : (tensor<*xf32>, tensor<?xi64>) -> tensor<*xf32>
        func.return %1 : tensor<*xf32>
      }"""
compiled = jitrt.compile(mlir_function, 'compute')
tensor = np.random.uniform(0, 10.0, size=(3, 3)).astype(np.float32)
perm0 = np.array([1, 0]).astype(np.int64)
perm1 = np.array([0, 1]).astype(np.int64)

[res] = jitrt.execute(compiled, [tensor, perm0, perm1])
np.testing.assert_allclose(
    res, np.transpose(np.transpose(tensor, perm0), perm1), atol=0.0)
