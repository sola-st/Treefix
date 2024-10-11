# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_metadata_ops_test.py
mlir_function = """
      func.func @test(%arg0: tensor<?xf32>) -> tensor<?xf32> {
        %0 = "tf.StopGradient"(%arg0) : (tensor<?xf32>) -> tensor<?xf32>
        func.return %0 : tensor<?xf32>
      }"""
compiled = jitrt.compile(mlir_function, 'test')
arg0 = np.random.uniform(0.0, 1.0, size=(10)).astype(np.float32)
[res] = jitrt.execute(compiled, [arg0])
np.testing.assert_allclose(res, arg0, rtol=0.0)
