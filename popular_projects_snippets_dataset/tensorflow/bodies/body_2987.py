# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_binary_bcast_test.py
mlir_function = """
      func.func @test(%arg0: tensor<?x?x12xf32>,
                      %arg1: tensor<?x?x12xf32>) -> tensor<?x?x12xf32> {
        %0 = "tf.AddV2"(%arg0, %arg1)
             : (tensor<?x?x12xf32>, tensor<?x?x12xf32>) -> tensor<?x?x12xf32>
        func.return %0 : tensor<?x?x12xf32>
      }"""

d0 = np.random.randint(1, 10)
d1 = np.random.randint(1, 10)

arg0 = np.random.uniform(0, 10.0, size=(d0, d1, 12)).astype(np.float32)
arg1 = np.random.uniform(0, 10.0, size=(d0, d1, 12)).astype(np.float32)

for specialize in specializations:
    for vectorize in [True, False]:
        compiled = jitrt.compile(mlir_function, 'test', specialize, vectorize)

        [res] = jitrt.execute(compiled, [arg0, arg1])
        np.testing.assert_allclose(res, arg0 + arg1, atol=0.0)
