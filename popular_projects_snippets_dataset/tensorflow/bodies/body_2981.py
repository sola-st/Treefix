# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_cast_test.py
mlir_function = """
      func.func @test(%arg0: tensor<?xi32>) -> tensor<?xui32> {
        %0 = "tf.Cast"(%arg0) : (tensor<?xi32>) -> tensor<?xui32>
        func.return %0 : tensor<?xui32>
      }"""

compiled = jitrt.compile(mlir_function, 'test')

arg0 = np.random.uniform(300, 3000, size=10).astype(np.int32)

[res] = jitrt.execute(compiled, [arg0])
np.testing.assert_equal(res, arg0)
np.testing.assert_equal(res.dtype, np.uint32)
