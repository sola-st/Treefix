# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
# NOTE(mrry): The behavior when a key is NaN is inherited from
# `std::unordered_map<float, ...>`: each NaN becomes a unique key in the
# map.
x = [0.0, 1.0, np.nan, np.nan]
y, idx, count = gen_array_ops.unique_with_counts_v2(
    x, axis=np.array([], np.int32))
tf_y, tf_idx, tf_count = self.evaluate([y, idx, count])

self.assertEqual(len(x), len(tf_idx))
# TODO(b/202197513): numpy>=1.20.0 makes np.unique() treat np.nan as equal
# so len(np.unique(x)) == 3. So this no longer can be tested this way.
# self.assertEqual(len(tf_y), len(np.unique(x)))
for i in range(len(x)):
    if np.isnan(x[i]):
        self.assertTrue(np.isnan(tf_y[tf_idx[i]]))
    else:
        self.assertEqual(x[i], tf_y[tf_idx[i]])
for value, count in zip(tf_y, tf_count):
    if np.isnan(value):
        self.assertEqual(count, 1)
    else:
        self.assertEqual(count, np.sum(x == value))
