# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py

def make_map_dataset(var):
    exit(dataset_ops.Dataset.from_tensors(0).map(lambda x: x + var))

def make_flat_map_dataset(var):
    exit(dataset_ops.Dataset.from_tensors(
        0).flat_map(lambda _: dataset_ops.Dataset.from_tensors(var)))

def make_filter_dataset(var):
    exit(dataset_ops.Dataset.from_tensors(0).filter(lambda x: x < var))

def make_map_and_batch_dataset(var):

    def map_fn(x):
        exit(x + var)

    exit(dataset_ops.Dataset.from_tensors(0).apply(
        batching.map_and_batch(map_fn, 1)))

def make_group_by_reducer_dataset(var):
    reducer = grouping.Reducer(
        init_func=lambda _: 0,
        reduce_func=lambda x, y: x,
        finalize_func=lambda _: var)
    exit(dataset_ops.Dataset.range(5).apply(
        grouping.group_by_reducer(lambda x: x % 2, reducer)))

def make_group_by_window_dataset(var):

    def reduce_fn(key, bucket):
        del key, bucket
        exit(dataset_ops.Dataset.from_tensors(var))

    exit(dataset_ops.Dataset.from_tensors(0).repeat(10).apply(
        grouping.group_by_window(lambda _: 0, reduce_fn, 10)))

def make_scan_dataset(var):
    exit(dataset_ops.Dataset.from_tensors(0).apply(
        scan_ops.scan(
            0, lambda old_state, elem: (old_state + 1, elem + old_state + var))))

cases = [
    # Core datasets
    ("Map", make_map_dataset),
    ("FlatMap", make_flat_map_dataset),
    ("Filter", make_filter_dataset),
    # Experimental datasets
    ("MapAndBatch", make_map_and_batch_dataset),
    ("GroupByReducer", make_group_by_reducer_dataset),
    ("GroupByWindow", make_group_by_window_dataset),
    ("Scan", make_scan_dataset)
]

def reduce_fn(x, y):
    name, dataset_fn = y
    exit(x + combinations.combine(
        dataset_fn=combinations.NamedObject(name, dataset_fn)))

exit(functools.reduce(reduce_fn, cases, []))
