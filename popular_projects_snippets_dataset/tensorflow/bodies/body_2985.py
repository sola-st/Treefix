# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_binary_bcast_test.py
mlir_function = """
      func.func @test(%arg0: tensor<?x?xf32>,
                      %arg1: tensor<?x?xf32>) -> tensor<?x?xf32> {
        %0 = "tf.Mul"(%arg0, %arg1)
             : (tensor<?x?xf32>, tensor<?x?xf32>) -> tensor<?x?xf32>
        func.return %0 : tensor<?x?xf32>
      }"""

m = np.random.randint(1, 10)
n = np.random.randint(1, 10)

lhs0 = np.random.uniform(0, 10.0, size=(1, 1)).astype(np.float32)
lhs1 = np.random.uniform(0, 10.0, size=(1, n)).astype(np.float32)
lhs2 = np.random.uniform(0, 10.0, size=(m, 1)).astype(np.float32)
lhs3 = np.random.uniform(0, 10.0, size=(m, n)).astype(np.float32)

rhs0 = np.random.uniform(0, 10.0, size=(1, 1)).astype(np.float32)
rhs1 = np.random.uniform(0, 10.0, size=(1, n)).astype(np.float32)
rhs2 = np.random.uniform(0, 10.0, size=(m, 1)).astype(np.float32)
rhs3 = np.random.uniform(0, 10.0, size=(m, n)).astype(np.float32)

for specialize in specializations:
    compiled = jitrt.compile(mlir_function, 'test', specialize)

    for lhs in [lhs0, lhs1, lhs2, lhs3]:
        for rhs in [rhs0, rhs1, rhs2, rhs3]:
            [res] = jitrt.execute(compiled, [lhs, rhs])
            np.testing.assert_allclose(res, lhs * rhs, atol=1e-07)
