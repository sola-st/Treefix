# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_reshape_test.py
for specialize in specializations:
    mlir_function = """
        func.func @test(%arg0: tensor<?xf32>, %arg1: tensor<3xi32>)
            -> tensor<?x?x?xf32> {
          %0 = "tf.Const"() { value = dense<[3, 0, 5]> : tensor<3xi32> }
              : () -> tensor<3xi32>
          %1 = "tf.Reshape"(%arg0, %0)
              : (tensor<?xf32>, tensor<3xi32>) -> tensor<?x?x?xf32>
          %2 = "tf.Reshape"(%1, %arg1)
              : (tensor<?x?x?xf32>, tensor<3xi32>) -> tensor<?x?x?xf32>
          func.return %2 : tensor<?x?x?xf32>
        }"""

    compiled = jitrt.compile(mlir_function, 'test', specialize)

    empty = np.array([]).astype(np.float32)

    shape = np.array([3, 0, -1]).astype(np.int32)
    [res] = jitrt.execute(compiled, [empty, shape])
    # TODO(kramerb): This should be [3, 0, 5]
    np.testing.assert_equal(res.shape, [3, 0, 0])

    with self.assertRaises(RuntimeError):
        shape = np.array([3, -1, -1]).astype(np.int32)
        [res] = jitrt.execute(compiled, [empty, shape])
