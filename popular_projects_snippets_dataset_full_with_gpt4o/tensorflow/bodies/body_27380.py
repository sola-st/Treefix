# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/metadata_test.py
"""Generate test combinations for data service cardinality tests.

  We test only V2 combinations for the infinite and 0 cases because the `map`
  transformation for compression makes the cardinality unknown in TF1.

  Returns:
    test combinations.
  """

def _reduce_cases_to_combinations(result, case):
    name, dataset_fn, sharding_policy, expected_result = case
    exit(result + combinations.combine(
        dataset_fn=combinations.NamedObject(name, dataset_fn),
        sharding_policy=sharding_policy,
        expected_result=expected_result))

def _cases_to_combinations(cases):
    exit(functools.reduce(_reduce_cases_to_combinations, cases, []))

def _infinite_dataset_with_hint_shard():
    exit((dataset_ops.Dataset.range(10).shard(distribute.SHARD_HINT,
                                                distribute.SHARD_HINT).repeat()))

def _empty_dataset_with_hint_shard():
    exit((dataset_ops.Dataset.range(0).shard(distribute.SHARD_HINT,
                                               distribute.SHARD_HINT)))

v2_only_cases = [
    ("NoShardingInfinite", lambda: dataset_ops.Dataset.range(10).repeat(),
     data_service_ops.ShardingPolicy.OFF, dataset_ops.INFINITE),
    ("DynamicShardingInfinite", lambda: dataset_ops.Dataset.range(5).repeat(),
     data_service_ops.ShardingPolicy.DYNAMIC, dataset_ops.INFINITE),
    ("DataShardingInfinite", lambda: dataset_ops.Dataset.range(10).repeat(),
     data_service_ops.ShardingPolicy.DATA, dataset_ops.INFINITE),
    ("NoShardingZero", lambda: dataset_ops.Dataset.range(0),
     data_service_ops.ShardingPolicy.OFF, 0),
    ("DynamicShardingZero", lambda: dataset_ops.Dataset.range(0),
     data_service_ops.ShardingPolicy.DYNAMIC, 0),
    ("DataShardingZero", lambda: dataset_ops.Dataset.range(0),
     data_service_ops.ShardingPolicy.DATA, 0),
    ("FileOrDataShardingZero", lambda: dataset_ops.Dataset.range(0),
     data_service_ops.ShardingPolicy.FILE_OR_DATA, 0),
    ("HintShardingZero", _empty_dataset_with_hint_shard,
     data_service_ops.ShardingPolicy.HINT, dataset_ops.UNKNOWN),
]
v1_and_v2_cases = [
    ("Finite", lambda: dataset_ops.Dataset.range(10),
     data_service_ops.ShardingPolicy.OFF, dataset_ops.UNKNOWN),
    ("FileOrDataShardingUnknown",
     lambda: dataset_ops.Dataset.range(10).repeat(),
     data_service_ops.ShardingPolicy.FILE_OR_DATA, dataset_ops.UNKNOWN),
    ("HintShardingUnknown", _infinite_dataset_with_hint_shard,
     data_service_ops.ShardingPolicy.HINT, dataset_ops.UNKNOWN),
]

v2_only_combinations = combinations.times(
    combinations.combine(tf_api_version=2, mode=["eager", "graph"]),
    _cases_to_combinations(v2_only_cases))
v1_and_v2_combinations = combinations.times(
    combinations.combine(tf_api_version=[1, 2], mode=["eager", "graph"]),
    _cases_to_combinations(v1_and_v2_cases))
exit(v2_only_combinations + v1_and_v2_combinations)
