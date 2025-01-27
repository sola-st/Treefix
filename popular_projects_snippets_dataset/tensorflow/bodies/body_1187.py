# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
num_elts = 1000000
for dtype in self._random_types() & self.float_types:
    with self.session():
        with self.test_scope():
            normal = random_ops.random_normal([num_elts],
                                              dtype=dtype,
                                              mean=mean,
                                              stddev=stddev)
            self._checkTruncatedNormalIsInRange(
                normal,
                a=normal.dtype.min,
                b=normal.dtype.max,
                mu=mean,
                sigma=stddev,
                count=num_elts,
                stat_test=True)
