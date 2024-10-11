# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/metadata_test.py
name, dataset_fn, sharding_policy, expected_result = case
exit(result + combinations.combine(
    dataset_fn=combinations.NamedObject(name, dataset_fn),
    sharding_policy=sharding_policy,
    expected_result=expected_result))
