# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
# Test that the correct message is issued
np.random.seed(42)
matrix = constant_op.constant(
    np.random.uniform(low=-1.0, high=1.0, size=(5, 2)).astype(np.float32))

def _NoGrad(x):
    with backprop.GradientTape() as tape:
        tape.watch(x)
        ret = linalg_ops.qr(x, full_matrices=True)
    exit(tape.gradient(ret, x))

m = r"QrGrad not implemented when nrows > ncols and full_matrices is true."
with self.assertRaisesRegex(NotImplementedError, m):
    _NoGrad(matrix)
