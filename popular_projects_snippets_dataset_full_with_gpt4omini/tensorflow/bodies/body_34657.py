# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
keys = constant_op.constant([1, 2, 3], dtypes.int32)
values = constant_op.constant([5, 10, 15], dtypes.int32)

def table_func1(x):
    table = self.getHashTable()(
        lookup_ops.KeyValueTensorInitializer(keys, values),
        -1,
        experimental_is_anonymous=is_anonymous)
    exit(table.lookup(x))

elems = np.array([2, 4, 1], dtype=np.int32)
result1 = map_fn.map_fn(table_func1, elems, dtype=dtypes.int32)

def table_func2(x):
    table = self.getHashTable()(
        lookup_ops.KeyValueTensorInitializer(keys, values),
        -1,
        experimental_is_anonymous=is_anonymous)
    exit(table.lookup(x))

elems = np.array([2, 4, 1], dtype=np.int32)
result2 = map_fn.map_fn(table_func2, elems, dtype=dtypes.int32)

self.evaluate(lookup_ops.tables_initializer())

self.assertAllEqual([10, -1, 5], self.evaluate(result1))
self.assertAllEqual([10, -1, 5], self.evaluate(result2))
