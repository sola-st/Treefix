# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_broadcast_to_test.py
mlir_function = """
      func.func @test(%arg0: tensor<?xf32>, %arg1: tensor<2xi32>)
           -> (tensor<?x?xf32>, tensor<?x?xf32>) {
        %1 = "tf.BroadcastTo"(%arg0, %arg1)
             : (tensor<?xf32>, tensor<2xi32>) -> tensor<?x?xf32>
        %2 = "tf.Add"(%1, %1)
             : (tensor<?x?xf32>, tensor<?x?xf32>) -> tensor<?x?xf32>
        func.return %1, %2 : tensor<?x?xf32>, tensor<?x?xf32>
      }"""

compiled = jitrt.compile(mlir_function, 'test')

arg0 = np.random.uniform(0, 10.0, size=1).astype(np.float32)
arg1 = np.random.uniform(0, 10, size=2).astype(np.int32)

[res1, res2] = jitrt.execute(compiled, [arg0, arg1])
np.testing.assert_allclose(res1, np.broadcast_to(arg0, arg1), atol=0.0)
np.testing.assert_allclose(res2, np.broadcast_to(arg0, arg1) * 2, atol=0.0)
