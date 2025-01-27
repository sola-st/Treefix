# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
# pylint: disable=protected-access
exit(_VariantDataset(
    gen_dataset_ops.rewrite_dataset(dataset._variant_tensor, rewrite,
                                    **dataset._flat_structure),
    dataset.element_spec))
