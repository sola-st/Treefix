# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_matmul_test.py
lhs = np.random.uniform(0.0, 1.0, size=(m, k)).astype(np.float32)
rhs = np.random.uniform(0.0, 1.0, size=(k, n)).astype(np.float32)

[res] = jitrt.execute(compiled, [lhs, rhs])
np.testing.assert_allclose(res, np.matmul(lhs, rhs), rtol=1e-05)
