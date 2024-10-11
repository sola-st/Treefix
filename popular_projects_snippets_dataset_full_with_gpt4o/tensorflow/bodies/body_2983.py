# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_cast_test.py
mlir_function = """
      func.func @test(%arg0: tensor<?xi64>) -> tensor<?xui8> {
        %0 = "tf.Cast"(%arg0) : (tensor<?xi64>) -> tensor<?xui8>
        func.return %0 : tensor<?xui8>
      }"""

compiled = jitrt.compile(mlir_function, 'test')

arg0 = np.random.uniform(300, 3000, size=10).astype(np.int64)

[res] = jitrt.execute(compiled, [arg0])
np.testing.assert_equal(res, arg0.astype(np.uint8))
np.testing.assert_equal(res.dtype, np.uint8)
