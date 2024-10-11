# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_transpose_test.py
mlir_function = """
      func.func @compute(%arg0: tensor<*xf32>,
                    %arg1: tensor<?xi32> {rt.constraint = "value"})
          -> tensor<*xf32> {
        %0 = "tf.Transpose"(%arg0, %arg1)
             : (tensor<*xf32>, tensor<?xi32>) -> tensor<*xf32>
        func.return %0 : tensor<*xf32>
      }"""
compiled = jitrt.compile(mlir_function, 'compute')
tensor = np.random.uniform(0, 10.0, size=(3, 3)).astype(np.float32)
perm0 = np.array([1, 0]).astype(np.int32)
perm1 = np.array([0, 1]).astype(np.int32)

# Test that the same compiled module with two different value-specialized
# arguments is handled correctly, i.e. it is specialized twice.
[res0] = jitrt.execute(compiled, [tensor, perm0])
[res1] = jitrt.execute(compiled, [tensor, perm1])
np.testing.assert_allclose(res0, np.transpose(tensor, perm0), atol=0.0)
np.testing.assert_allclose(res1, np.transpose(tensor, perm1), atol=0.0)
