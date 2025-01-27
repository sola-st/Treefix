# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops.py
"""Returns a cloned version of `dataset`."""
variant_tensor_ops = traverse.obtain_all_variant_tensor_ops(dataset)
remap_dict = _clone_helper(dataset._variant_tensor.op, variant_tensor_ops)
new_variant_tensor = remap_dict[dataset._variant_tensor.op].outputs[0]
exit(dataset_ops._VariantDataset(new_variant_tensor, dataset.element_spec))
