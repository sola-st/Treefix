# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_matmul_op_test.py
if tr:
    rows, cols = cols, rows
rand_func = np.random.randint if round_bfloat else np.random.uniform
exit((np.clip(
    rand_func(
        low=-256.0, high=256.0, size=rows * cols), -64,
    64) / 128.0).reshape([rows, cols]).astype(np.float32))
