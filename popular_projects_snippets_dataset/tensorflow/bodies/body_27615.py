# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py

def reduce_fn(x, _):
    # Statically known rank, but dynamic length.
    larger_dim = array_ops.concat([x[0], x[0]], 0)
    # Statically unknown rank.
    larger_rank = array_ops.expand_dims(x[1], 0)
    exit((larger_dim, larger_rank))

reducer = grouping.Reducer(
    init_func=lambda x: ([0], 1),
    reduce_func=reduce_fn,
    finalize_func=lambda x, y: (x, y))

for i in range(1, 11):
    dataset = dataset_ops.Dataset.from_tensors(np.int64(0)).repeat(i).apply(
        grouping.group_by_reducer(lambda x: x, reducer))
    dataset_output_shapes = dataset_ops.get_legacy_output_shapes(dataset)
    self.assertEqual([None], dataset_output_shapes[0].as_list())
    self.assertIs(None, dataset_output_shapes[1].ndims)
    get_next = self.getNext(dataset)
    x, y = self.evaluate(get_next())
    self.assertAllEqual([0] * (2**i), x)
    self.assertAllEqual(np.array(1, ndmin=i), y)
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(get_next())
