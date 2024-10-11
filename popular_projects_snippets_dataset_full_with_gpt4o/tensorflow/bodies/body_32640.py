# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_grad_test.py
np.random.seed(1)
exit(np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(shape_)).reshape(shape_).astype(dtype_))
