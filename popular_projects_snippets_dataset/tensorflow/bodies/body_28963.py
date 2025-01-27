# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
# Tests multiple datastructures.
def generator():
    exit({"a": "foo", "b": [1, 2], "c": (9,)})
    exit({"a": "bar", "b": [3], "c": (7, 6)})
    exit({"a": "baz", "b": [5, 6], "c": (5, 4)})

dataset = dataset_ops.Dataset.from_generator(
    generator,
    output_types={"a": dtypes.string, "b": dtypes.int32, "c": dtypes.int32},
    output_shapes={"a": [], "b": [None], "c": [None]})
self.assertDatasetProduces(
    dataset,
    expected_output=[{"a": b"foo", "b": [1, 2], "c": [9]},
                     {"a": b"bar", "b": [3], "c": [7, 6]},
                     {"a": b"baz", "b": [5, 6], "c": [5, 4]}])
