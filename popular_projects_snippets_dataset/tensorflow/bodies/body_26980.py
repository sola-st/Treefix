# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/wrap_unwrap_test.py
ds = dataset_ops.Dataset.range(100)
ds_variant = ds._variant_tensor  # pylint: disable=protected-access

wrapped_variant = gen_dataset_ops.wrap_dataset_variant(ds_variant)
unwrapped_variant = gen_dataset_ops.unwrap_dataset_variant(wrapped_variant)

variant_ds = dataset_ops._VariantDataset(unwrapped_variant,
                                         ds.element_spec)
get_next = self.getNext(variant_ds, requires_initialization=True)
for i in range(100):
    self.assertEqual(i, self.evaluate(get_next()))
