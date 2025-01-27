# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_matmul_test.py
compiled = jitrt.compile(
    matmul(), "matmul", vectorize=True, enable_xla_cpu_transformations=True)
for _ in range(100):
    m = np.random.randint(1, 10)
    k = np.random.randint(1, 10)
    verify_matmul(compiled, m, k, 1)
