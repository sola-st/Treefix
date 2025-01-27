# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for use_gpu in [False, True]:
    with self.session(use_gpu=use_gpu):
        shape = [2, 3, 4]
        rnd1 = random_ops.random_normal(shape, 0.0, 1.0, dtypes.float32)
        rnd2 = random_ops.random_normal(shape, 0.0, 1.0, dtypes.float32)
        diff = rnd2 - rnd1
        self.assertTrue(np.linalg.norm(diff.eval()) > 0.1)
