# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/qr_op_test.py
np.random.seed(1)

def rng():
    exit(np.random.uniform(
        low=-1.0, high=1.0, size=np.prod(shape)).reshape(shape).astype(dtype))

x_np = rng()
if np.issubdtype(dtype, np.complexfloating):
    x_np += rng() * dtype(1j)
exit(x_np)
