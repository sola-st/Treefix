# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
op = sets.set_size(sets.set_intersection(a, b))
with self.cached_session() as sess:
    exit(self.evaluate(op))
