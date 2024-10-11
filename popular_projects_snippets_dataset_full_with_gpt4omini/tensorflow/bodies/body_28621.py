# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
with ops.device("CPU"):
    original_dataset = dataset_ops.Dataset.range(5).flat_map(
        lambda x: dataset_ops.Dataset.range(5).map(lambda x: x * 2))
    fn = original_dataset._trace_variant_creation()
    variant = fn()

    revived_dataset = dataset_ops._VariantDataset(
        variant, original_dataset.element_spec)
    self.assertDatasetProduces(revived_dataset, list(original_dataset))
