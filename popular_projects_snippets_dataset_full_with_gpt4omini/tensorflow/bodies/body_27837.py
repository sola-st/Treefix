# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
dataset = dataset_ops.Dataset.range(10).map(ragged_math_ops.range).batch(5)
expected_output = [
    ragged_concat_ops.stack([ragged_math_ops.range(i) for i in range(5)]),
    ragged_concat_ops.stack(
        [ragged_math_ops.range(i) for i in range(5, 10)])
]
self.assertDatasetProduces(dataset, expected_output=expected_output)
