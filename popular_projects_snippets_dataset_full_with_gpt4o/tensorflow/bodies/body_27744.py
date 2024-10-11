# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
with self.assertRaisesRegex(ValueError, r"should have the same length"):
    dataset_ops.Dataset.sample_from_datasets(
        [dataset_ops.Dataset.range(10),
         dataset_ops.Dataset.range(20)],
        weights=[0.25, 0.25, 0.25, 0.25])

with self.assertRaisesRegex(TypeError, "`tf.float32` or `tf.float64`"):
    dataset_ops.Dataset.sample_from_datasets(
        [dataset_ops.Dataset.range(10),
         dataset_ops.Dataset.range(20)],
        weights=[1, 1])

with self.assertRaisesRegex(TypeError, "must have compatible"):
    dataset_ops.Dataset.sample_from_datasets([
        dataset_ops.Dataset.from_tensors(0),
        dataset_ops.Dataset.from_tensors(0.0)
    ])

with self.assertRaisesRegex(
    ValueError, r"Invalid `datasets`. `datasets` should not be empty."):
    dataset_ops.Dataset.sample_from_datasets(datasets=[], weights=[])
