# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_reshape_test.py
for specialize in specializations:
    mlir_function = """
        func.func @test(%arg0: tensor<?x?xf32>, %arg1: tensor<1xi32>)
            -> tensor<?xf32> {
          %0 = "tf.Reshape"(%arg0, %arg1)
              : (tensor<?x?xf32>, tensor<1xi32>) -> tensor<?xf32>
          func.return %0 : tensor<?xf32>
        }"""

    compiled = jitrt.compile(mlir_function, 'test', specialize)

    d0 = np.random.randint(1, 10) * 2
    d1 = np.random.randint(1, 10) * 2

    arg0 = np.random.uniform(0, 10.0, size=(d0, d1)).astype(np.float32)

    shape = np.array([d0 * d1]).astype(np.int32)
    [res] = jitrt.execute(compiled, [arg0, shape])
    np.testing.assert_allclose(res, np.reshape(arg0, shape), atol=0.0)

    shape = np.array([-1]).astype(np.int32)
    [res] = jitrt.execute(compiled, [arg0, shape])
    np.testing.assert_allclose(res, np.reshape(arg0, shape), atol=0.0)

    with self.assertRaises(RuntimeError):
        shape = np.array([d0]).astype(np.int32)
        [res] = jitrt.execute(compiled, [arg0, shape])
