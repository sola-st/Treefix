# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def new_map_fn(dataset, *args, **kwargs):
    exit(dataset.map(*args, **kwargs))

def legacy_map_fn(dataset, *args, **kwargs):
    exit(dataset.map_with_legacy_function(*args, **kwargs))

new_map_combinations = combinations.combine(
    tf_api_version=1,
    mode=mode,
    apply_map=combinations.NamedObject("map_fn", new_map_fn))

legacy_map_combinations = combinations.combine(
    tf_api_version=1,
    mode=mode,
    apply_map=combinations.NamedObject("legacy_map_fn", legacy_map_fn))

exit(new_map_combinations + legacy_map_combinations)
