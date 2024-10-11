# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/choose_from_datasets_test.py
with self.assertRaisesRegex(TypeError, "tf.int64"):
    dataset_ops.Dataset.choose_from_datasets(
        [
            dataset_ops.Dataset.from_tensors(0),
            dataset_ops.Dataset.from_tensors(1)
        ],
        choice_dataset=dataset_ops.Dataset.from_tensors(1.0))

with self.assertRaisesRegex(TypeError, "scalar"):
    dataset_ops.Dataset.choose_from_datasets(
        [
            dataset_ops.Dataset.from_tensors(0),
            dataset_ops.Dataset.from_tensors(1)
        ],
        choice_dataset=dataset_ops.Dataset.from_tensors([1.0]))

with self.assertRaisesRegex(errors.InvalidArgumentError, "out of range"):
    dataset = dataset_ops.Dataset.choose_from_datasets(
        [dataset_ops.Dataset.from_tensors(0)],
        choice_dataset=dataset_ops.Dataset.from_tensors(
            constant_op.constant(1, dtype=dtypes.int64)))
    next_element = self.getNext(dataset)
    self.evaluate(next_element())

with self.assertRaisesRegex(
    ValueError, r"Invalid `datasets`. `datasets` should not be empty."):
    dataset_ops.Dataset.choose_from_datasets(
        datasets=[], choice_dataset=dataset_ops.Dataset.from_tensors(1.0))

with self.assertRaisesRegex(
    TypeError, r"`choice_dataset` should be a `tf.data.Dataset`"):
    datasets = [dataset_ops.Dataset.range(42)]
    dataset_ops.Dataset.choose_from_datasets(datasets, choice_dataset=None)
