# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cardinality_test.py
v1_only_cases = [
    ("Map1", lambda: dataset_ops.Dataset.range(5).map(lambda x: x),
     dataset_ops.UNKNOWN),
    ("Map2", lambda: dataset_ops.Dataset.range(5).map(
        lambda x: x, num_parallel_calls=1), dataset_ops.UNKNOWN),
]
v2_only_cases = [
    ("Map1", lambda: dataset_ops.Dataset.range(5).map(lambda x: x), 5),
    ("Map2", lambda: dataset_ops.Dataset.range(5).map(
        lambda x: x, num_parallel_calls=1), 5),
]
v1_and_v2_cases = [
    ("Batch1",
     lambda: dataset_ops.Dataset.range(5).batch(2, drop_remainder=True), 2),
    ("Batch2",
     lambda: dataset_ops.Dataset.range(5).batch(2, drop_remainder=False), 3),
    ("Batch3",
     lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).batch(2),
     dataset_ops.UNKNOWN),
    ("Batch4", lambda: dataset_ops.Dataset.range(5).repeat().batch(2),
     dataset_ops.INFINITE),
    ("Cache1", lambda: dataset_ops.Dataset.range(5).cache(), 5),
    ("Cache2", lambda: dataset_ops.Dataset.range(5).cache("foo"), 5),
    ("Concatenate1", lambda: dataset_ops.Dataset.range(5).concatenate(
        dataset_ops.Dataset.range(5)), 10),
    ("Concatenate2",
     lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).concatenate(
         dataset_ops.Dataset.range(5)), dataset_ops.UNKNOWN),
    ("Concatenate3", lambda: dataset_ops.Dataset.range(5).repeat().
     concatenate(dataset_ops.Dataset.range(5)), dataset_ops.INFINITE),
    ("Concatenate4", lambda: dataset_ops.Dataset.range(5).concatenate(
        dataset_ops.Dataset.range(5).filter(lambda _: True)),
     dataset_ops.UNKNOWN),
    ("Concatenate5",
     lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).concatenate(
         dataset_ops.Dataset.range(5).filter(lambda _: True)),
     dataset_ops.UNKNOWN),
    ("Concatenate6", lambda: dataset_ops.Dataset.range(5).repeat().
     concatenate(dataset_ops.Dataset.range(5).filter(lambda _: True)),
     dataset_ops.INFINITE),
    ("Concatenate7", lambda: dataset_ops.Dataset.range(5).concatenate(
        dataset_ops.Dataset.range(5).repeat()), dataset_ops.INFINITE),
    ("Concatenate8",
     lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).concatenate(
         dataset_ops.Dataset.range(5).repeat()), dataset_ops.INFINITE),
    ("Concatenate9",
     lambda: dataset_ops.Dataset.range(5).repeat().concatenate(
         dataset_ops.Dataset.range(5).repeat()), dataset_ops.INFINITE),
    ("FlatMap", lambda: dataset_ops.Dataset.range(5).flat_map(
        lambda _: dataset_ops.Dataset.from_tensors(0)), dataset_ops.UNKNOWN),
    ("Filter", lambda: dataset_ops.Dataset.range(5).filter(lambda _: True),
     dataset_ops.UNKNOWN),
    ("FromTensors1", lambda: dataset_ops.Dataset.from_tensors(0), 1),
    ("FromTensors2", lambda: dataset_ops.Dataset.from_tensors((0, 1)), 1),
    ("FromTensorSlices1",
     lambda: dataset_ops.Dataset.from_tensor_slices([0, 0, 0]), 3),
    ("FromTensorSlices2", lambda: dataset_ops.Dataset.from_tensor_slices(
        ([0, 0, 0], [1, 1, 1])), 3),
    ("Interleave1", lambda: dataset_ops.Dataset.range(5).interleave(
        lambda _: dataset_ops.Dataset.from_tensors(0), cycle_length=1),
     dataset_ops.UNKNOWN),
    ("Interleave2", lambda: dataset_ops.Dataset.range(5).interleave(
        lambda _: dataset_ops.Dataset.from_tensors(0),
        cycle_length=1,
        num_parallel_calls=1), dataset_ops.UNKNOWN),
    ("Interleave3", lambda: dataset_ops.Dataset.range(5).repeat().interleave(
        lambda _: dataset_ops.Dataset.from_tensors(0),
        cycle_length=1,
        num_parallel_calls=1), dataset_ops.INFINITE),
    ("PaddedBatch1", lambda: dataset_ops.Dataset.range(5).padded_batch(
        2, [], drop_remainder=True), 2),
    ("PaddedBatch2", lambda: dataset_ops.Dataset.range(5).padded_batch(
        2, [], drop_remainder=False), 3),
    ("PaddedBatch3", lambda: dataset_ops.Dataset.range(5).filter(
        lambda _: True).padded_batch(2, []), dataset_ops.UNKNOWN),
    ("PaddedBatch4",
     lambda: dataset_ops.Dataset.range(5).repeat().padded_batch(2, []),
     dataset_ops.INFINITE),
    ("Prefetch", lambda: dataset_ops.Dataset.range(5).prefetch(buffer_size=1),
     5),
    ("Range1", lambda: dataset_ops.Dataset.range(0), 0),
    ("Range2", lambda: dataset_ops.Dataset.range(5), 5),
    ("Range3", lambda: dataset_ops.Dataset.range(5, 10), 5),
    ("Range4", lambda: dataset_ops.Dataset.range(10, 5), 0),
    ("Range5", lambda: dataset_ops.Dataset.range(5, 10, 2), 3),
    ("Range6", lambda: dataset_ops.Dataset.range(10, 5, -2), 3),
    ("Range7", lambda: dataset_ops.Dataset.range(0, 0, -2), 0),
    ("Range8", lambda: dataset_ops.Dataset.range(3, 3, 1), 0),
    ("Range9", lambda: dataset_ops.Dataset.range(-4, -4, 2), 0),
    ("Range10", lambda: dataset_ops.Dataset.range(1, 0, 3), 0),
    ("Range11", lambda: dataset_ops.Dataset.range(0, 1, -3), 0),
    ("Repeat1", lambda: dataset_ops.Dataset.range(0).repeat(0), 0),
    ("Repeat2", lambda: dataset_ops.Dataset.range(1).repeat(0), 0),
    ("Repeat3", lambda: dataset_ops.Dataset.range(0).repeat(5), 0),
    ("Repeat4", lambda: dataset_ops.Dataset.range(1).repeat(5), 5),
    ("Repeat5", lambda: dataset_ops.Dataset.range(0).repeat(), 0),
    ("Repeat6", lambda: dataset_ops.Dataset.range(1).repeat(),
     dataset_ops.INFINITE),
    ("Shuffle", lambda: dataset_ops.Dataset.range(5).shuffle(buffer_size=1),
     5),
    ("Shard1", lambda: dataset_ops.Dataset.range(5).shard(2, 0), 3),
    ("Shard2", lambda: dataset_ops.Dataset.range(5).shard(8, 7), 0),
    ("Shard3",
     lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).shard(2, 0),
     dataset_ops.UNKNOWN),
    ("Shard4", lambda: dataset_ops.Dataset.range(5).repeat().shard(2, 0),
     dataset_ops.INFINITE),
    ("Skip1", lambda: dataset_ops.Dataset.range(5).skip(2), 3),
    ("Skip2", lambda: dataset_ops.Dataset.range(5).skip(8), 0),
    ("Skip3",
     lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).skip(2),
     dataset_ops.UNKNOWN),
    ("Skip4", lambda: dataset_ops.Dataset.range(5).repeat().skip(2),
     dataset_ops.INFINITE),
    ("Take1", lambda: dataset_ops.Dataset.range(5).take(2), 2),
    ("Take2", lambda: dataset_ops.Dataset.range(5).take(8), 5),
    ("Take3",
     lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).take(2),
     dataset_ops.UNKNOWN),
    ("Take4", lambda: dataset_ops.Dataset.range(5).repeat().take(2), 2),
    ("Window1", lambda: dataset_ops.Dataset.range(5).window(
        size=2, shift=2, drop_remainder=True), 2),
    ("Window2", lambda: dataset_ops.Dataset.range(5).window(
        size=2, shift=2, drop_remainder=False), 3),
    ("Zip1", lambda: dataset_ops.Dataset.zip(dataset_ops.Dataset.range(5)),
     5),
    ("Zip2", lambda: dataset_ops.Dataset.zip(
        (dataset_ops.Dataset.range(5), dataset_ops.Dataset.range(3))), 3),
    ("Zip3", lambda: dataset_ops.Dataset.zip((dataset_ops.Dataset.range(
        5), dataset_ops.Dataset.range(3).repeat())), 5),
    ("Zip4", lambda: dataset_ops.Dataset.zip(
        (dataset_ops.Dataset.range(5).repeat(), dataset_ops.Dataset.range(3).
         repeat())), dataset_ops.INFINITE),
    ("Zip5", lambda: dataset_ops.Dataset.zip(
        (dataset_ops.Dataset.range(5), dataset_ops.Dataset.range(3).filter(
            lambda _: True))), dataset_ops.UNKNOWN),
]
def reduce_cases_to_combinations(x, y):
    name, dataset_fn, expected_result = y
    exit(x + combinations.combine(
        dataset_fn=combinations.NamedObject(name, dataset_fn),
        expected_result=expected_result))

def cases_to_combinations(cases):
    exit(functools.reduce(reduce_cases_to_combinations, cases, []))

v1_only_combinations = combinations.times(
    combinations.combine(tf_api_version=1, mode=["eager", "graph"]),
    cases_to_combinations(v1_only_cases))
v2_only_combinations = combinations.times(
    combinations.combine(tf_api_version=2, mode=["eager", "graph"]),
    cases_to_combinations(v2_only_cases))
v1_and_v2_combinations = combinations.times(
    combinations.combine(tf_api_version=[1, 2], mode=["eager", "graph"]),
    cases_to_combinations(v1_and_v2_cases))

exit(v1_only_combinations + v2_only_combinations + v1_and_v2_combinations)
