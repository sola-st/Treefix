# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_binary_bcast_test.py
mlir_function = """
      func.func @test(%arg0: tensor<?x4xf32>,
                      %arg1: tensor<4xf32>,
                      %arg2: tensor<4xf32>) -> tensor<?x4xf32> {
        %0 = "tf.Log1p"(%arg0)
             : (tensor<?x4xf32>) -> tensor<?x4xf32>
        %1 = "tf.Sub"(%0, %arg1)
             : (tensor<?x4xf32>, tensor<4xf32>) -> tensor<?x4xf32>
        %2 = "tf.Mul"(%1, %arg2)
             : (tensor<?x4xf32>, tensor<4xf32>) -> tensor<?x4xf32>
        %3 = "tf.Atan2"(%2, %arg2)
             : (tensor<?x4xf32>, tensor<4xf32>) -> tensor<?x4xf32>
        func.return %3 : tensor<?x4xf32>
      }"""

n = np.random.randint(1, 10)

arg0 = np.random.uniform(0, 10.0, size=(n, 4)).astype(np.float32)
arg1 = np.random.uniform(0, 10.0, size=(4)).astype(np.float32)
arg2 = np.random.uniform(0, 10.0, size=(4)).astype(np.float32)

for specialize in specializations:
    for vectorize in [True, False]:
        compiled = jitrt.compile(mlir_function, 'test', specialize, vectorize)

        [res] = jitrt.execute(compiled, [arg0, arg1, arg2])
        ref = np.arctan2((np.log1p(arg0) - arg1) * arg2, arg2)
        np.testing.assert_allclose(res, ref, atol=1e-04)
