# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_binary_bcast_test.py
mlir_function = """
      func.func @compute(%arg0: tensor<?x4xf32>,
                         %arg1: tensor<4xf32>,
                         %arg2: tensor<f32>) -> tensor<?x4xf32> {
        %0 = "tf.AddV2"(%arg1, %arg2)
             : (tensor<4xf32>, tensor<f32>) -> tensor<4xf32>
        %1 = "tf.AddV2"(%arg0, %0)
             : (tensor<?x4xf32>, tensor<4xf32>) -> tensor<?x4xf32>
        %2 = "tf.AddV2"(%1, %0)
             : (tensor<?x4xf32>, tensor<4xf32>) -> tensor<?x4xf32>
        func.return %2 : tensor<?x4xf32>
      }"""

for specialize in specializations:
    compiled = jitrt.compile(mlir_function, 'compute', specialize)

    arg0 = np.random.uniform(0, 10.0, size=(1, 4)).astype(np.float32)
    arg1 = np.random.uniform(0, 10.0, size=(4)).astype(np.float32)
    arg2 = np.random.uniform(0, 10.0, size=()).astype(np.float32)

    [res] = jitrt.execute(compiled, [arg0, arg1, arg2])

    # Reference implementation with numpy
    t_0 = np.add(arg1, arg2)
    t_1 = np.add(arg0, t_0)
    t_2 = np.add(t_1, t_0)

    np.testing.assert_allclose(res, t_2, atol=0.0)
