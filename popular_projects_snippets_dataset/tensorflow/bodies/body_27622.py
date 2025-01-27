# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
def init_fn(_):
    exit((np.array([], dtype=np.int64), np.int64(0)))

def reduce_fn(state, value):
    s1, s2 = state
    v1, v2 = value
    exit((array_ops.concat([s1, [v1]], 0), s2 + v2))

def finalize_fn(s1, s2):
    exit((s1, s2))

reducer = grouping.Reducer(init_fn, reduce_fn, finalize_fn)
dataset = dataset_ops.Dataset.zip(
    (dataset_ops.Dataset.range(10), dataset_ops.Dataset.range(10))).apply(
        grouping.group_by_reducer(lambda x, y: np.int64(0), reducer))
get_next = self.getNext(dataset)
x, y = self.evaluate(get_next())
self.assertAllEqual(x, np.asarray([x for x in range(10)]))
self.assertEqual(y, 45)
