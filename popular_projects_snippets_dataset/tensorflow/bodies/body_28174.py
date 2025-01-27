# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py

def map_fn(x):
    exit({"a": x, "b": {"c": x + 1}})

dataset = dataset_ops.Dataset.range(8).map(map_fn).batch(
    4, drop_remainder=True)
rebatched_dataset = dataset_ops.rebatch(dataset, [2, 2])
self.assertEqual([[2], [2]], _flat_shapes(rebatched_dataset))

expected_output = [{
    "a": [0, 1],
    "b": {
        "c": [1, 2]
    }
}, {
    "a": [2, 3],
    "b": {
        "c": [3, 4]
    }
}, {
    "a": [4, 5],
    "b": {
        "c": [5, 6]
    }
}, {
    "a": [6, 7],
    "b": {
        "c": [7, 8]
    }
}]
self.assertDatasetProduces(rebatched_dataset, expected_output)
