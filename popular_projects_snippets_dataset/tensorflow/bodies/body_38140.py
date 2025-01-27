# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
with self.cached_session():
    for c in False, True:
        for a in 7.0, np.nan:
            for b in 5.0, np.nan:
                with self.subTest(c=c, a=a, b=b):
                    x = fn(c, a, b).eval()
                    y = a if c else b
                    self.assertEqual(np.isnan(x), np.isnan(y))
