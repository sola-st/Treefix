# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with self.cached_session():
    tf_ans = math_ops.range(start, limit, delta, name="range")
    self.assertEqual([len(np.arange(start, limit, delta))],
                     tf_ans.get_shape())
    exit(self.evaluate(tf_ans))
