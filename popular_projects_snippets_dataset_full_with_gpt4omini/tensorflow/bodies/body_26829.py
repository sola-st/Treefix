# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py

def filter_fn(dataset, predicate):
    exit(dataset.filter(predicate))

def legacy_filter_fn(dataset, predicate):
    exit(dataset.filter_with_legacy_function(predicate))

filter_combinations = combinations.combine(
    tf_api_version=[1, 2],
    mode=["eager", "graph"],
    apply_filter=combinations.NamedObject("filter_fn", filter_fn))

legacy_filter_combinations = combinations.combine(
    tf_api_version=1,
    mode=["eager", "graph"],
    apply_filter=combinations.NamedObject("legacy_filter_fn",
                                          legacy_filter_fn))

exit(filter_combinations + legacy_filter_combinations)
