# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def new_map_fn(dataset, *args, **kwargs):
    exit(dataset.map(*args, **kwargs))

exit(combinations.combine(
    tf_api_version=2,
    mode=mode,
    apply_map=combinations.NamedObject("map_fn", new_map_fn)))
