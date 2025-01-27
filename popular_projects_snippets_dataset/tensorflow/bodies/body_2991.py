# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_binary_bcast_test.py
mlir_function = """
      func.func @compute(%arg0: tensor<*xi32>,
                         %arg1: tensor<i32> {rt.constraint = "value"})
          -> tensor<*xi32> {
        %0 = "tf.AddV2"(%arg0, %arg1)
             : (tensor<*xi32>, tensor<i32>) -> tensor<*xi32>
        func.return %0 : tensor<*xi32>
      }"""
compiled = jitrt.compile(mlir_function, 'compute')
# Test that the same compiled module with two different value-specialized
# arguments is handled correctly.
tensor = np.random.uniform(0, 10.0, size=(3)).astype(np.int32)
rhs0 = np.random.uniform(0, 10.0, size=()).astype(np.int32)
rhs1 = np.random.uniform(0, 10.0, size=()).astype(np.int32)
[res0] = jitrt.execute(compiled, [tensor, rhs0])
[res1] = jitrt.execute(compiled, [tensor, rhs1])
np.testing.assert_allclose(res0, np.add(tensor, rhs0), atol=0.0)
np.testing.assert_allclose(res1, np.add(tensor, rhs1), atol=0.0)
