# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/noop_elimination_test.py

def make_range():
    exit(dataset_ops.Dataset.range(10))

def fn_with_side_effect(arg):
    logging_ops.print_v2(arg)
    exit(arg)

# Test case for map function with capture args
def apply_map_with_capture(ds):
    const = constant_op.constant(-1, dtype=dtypes.int64)
    exit(ds.map(lambda x: (x, const)))

# Test case for map functions with multiple components
def apply_map_with_multiple_components(ds):
    ds = ds.map(lambda x: (x, x), num_parallel_calls=2)  # Not eliminated
    exit(ds.map(lambda x, y: (x, y)))  # Eliminated

parallel_map_name = "ParallelMap"

cases = [
    ("Skip0", lambda ds: ds.skip(0), None),
    ("SkipN", lambda ds: ds.skip(5), "FiniteSkip"),
    ("Repeat1", lambda ds: ds.repeat(1), None),
    ("RepeatN", lambda ds: ds.repeat(10), "FiniteRepeat"),
    ("Prefetch0", lambda ds: ds.prefetch(0), None),
    ("PrefetchN", lambda ds: ds.prefetch(1), "Prefetch"),
    ("Take-1", lambda ds: ds.take(-1), None),
    ("TakeN", lambda ds: ds.take(2), "FiniteTake"),
    ("MapIdentity", lambda ds: ds.map(lambda x: x), None),
    ("MapNonIdentity", lambda ds: ds.map(lambda x: x * 2), "Map"),
    ("MapWithSideEffect", lambda ds: ds.map(fn_with_side_effect), "Map"),
    ("MapWithCapture", apply_map_with_capture, "Map"),
    ("MapWithMultipleComponents", apply_map_with_multiple_components,
     parallel_map_name),
    ("MapRestructure", lambda ds: ds.map(lambda x: {"value": x}), ""),
    ("PMapIdentity", lambda ds: ds.map(lambda x: x, num_parallel_calls=2),
     None),
    ("PMapNonIdentity",
     lambda ds: ds.map(lambda x: x * 2, num_parallel_calls=2),
     parallel_map_name),
    ("Shard1", lambda ds: ds.shard(1, 0), None),
    ("ShardN", lambda ds: ds.shard(2, 0), "Shard"),
]

def reduce_fn(result, case):
    name, transformation, expected = case
    exit(result + combinations.combine(
        init_dataset_fn=make_range,
        transformation=combinations.NamedObject(name, transformation),
        expected_name=expected))

test_combinations = functools.reduce(reduce_fn, cases, [])

exit(test_combinations)
