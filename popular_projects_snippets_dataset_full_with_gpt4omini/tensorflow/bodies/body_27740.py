# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
if rerandomize is not None and not tf_compat.forward_compatible(
    2022, 12, 17):
    self.skipTest(
        "target functionality not available due to forward compatibility")
dataset1 = dataset_ops.Dataset.range(0, 10)
dataset2 = dataset_ops.Dataset.range(100, 110)
sample_dataset = dataset_ops.Dataset.sample_from_datasets(
    [dataset1, dataset2],
    seed=42,
    weights=[0.5, 0.5],
    stop_on_empty_dataset=True,
    rerandomize_each_iteration=rerandomize)
first_epoch = self.getDatasetOutput(sample_dataset)
second_epoch = self.getDatasetOutput(sample_dataset)

if rerandomize:
    self.assertNotEqual(first_epoch, second_epoch)
else:
    self.assertEqual(first_epoch, second_epoch)
