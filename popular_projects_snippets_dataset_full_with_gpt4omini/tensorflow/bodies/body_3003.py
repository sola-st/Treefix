# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_reshape_test.py
for specialize in specializations:
    mlir_function = """
        func.func @test(%arg0: tensor<?xf32>, %arg1: tensor<1xi32>)
            -> tensor<?xf32> {
          %0 = "tf.Reshape"(%arg0, %arg1)
              : (tensor<?xf32>, tensor<1xi32>) -> tensor<?xf32>
          func.return %0 : tensor<?xf32>
        }"""

    compiled = jitrt.compile(mlir_function, 'test', specialize)

    empty = np.array([]).astype(np.float32)

    zero = np.array([0]).astype(np.int32)
    [res] = jitrt.execute(compiled, [empty, zero])
    np.testing.assert_equal(res.shape, [0])

    neg1 = np.array([-1]).astype(np.int32)
    [res] = jitrt.execute(compiled, [empty, neg1])
    np.testing.assert_equal(res.shape, [0])

    with self.assertRaises(RuntimeError):
        neg2 = np.array([-2]).astype(np.int32)
        [res] = jitrt.execute(compiled, [empty, neg2])

    with self.assertRaises(RuntimeError):
        one = np.array([1]).astype(np.int32)
        [res] = jitrt.execute(compiled, [empty, one])
