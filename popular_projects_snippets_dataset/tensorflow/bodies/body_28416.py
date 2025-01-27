# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
delta = array_ops.placeholder(dtype=dtypes.int64)

def reduce_fn(state, _):
    exit(state + delta)

for i in range(10):
    ds = dataset_ops.Dataset.range(1, i + 1)
    result = ds.reduce(np.int64(0), reduce_fn)
    with self.cached_session() as sess:
        square = sess.run(result, feed_dict={delta: i})
        self.assertEqual(i * i, square)
