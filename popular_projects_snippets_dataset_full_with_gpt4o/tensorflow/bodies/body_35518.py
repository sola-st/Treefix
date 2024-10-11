# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
with self.session():
    shape = [2, 3, 4]
    rnd1 = random_ops.truncated_normal(shape, 0.0, 1.0, dtypes.float32)
    rnd2 = random_ops.truncated_normal(shape, 0.0, 1.0, dtypes.float32)
    diff = rnd2 - rnd1
    self.assertTrue(np.linalg.norm(diff.eval()) > 0.1)
