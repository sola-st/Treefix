# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
with warnings.catch_warnings(record=True) as w:
    dataset = dataset_ops.Dataset.random(
        seed=42,
        rerandomize_each_iteration=rerandomize,
        name="random").take(10)
first_epoch = self.getDatasetOutput(dataset, requires_initialization=True)
second_epoch = self.getDatasetOutput(dataset, requires_initialization=True)
if rerandomize:
    if not tf2.enabled() and rerandomize:
        found_warning = False
        for warning in w:
            if ("In TF 1, the `rerandomize_each_iteration=True` option" in
                str(warning)):
                found_warning = True
                break
        self.assertTrue(found_warning)

self.assertEqual(first_epoch, second_epoch)
