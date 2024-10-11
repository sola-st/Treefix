# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/traverse_test.py
self._input_dataset = input_dataset
temp_variant_tensor = gen_dataset_ops.prefetch_dataset(
    input_dataset._variant_tensor,
    buffer_size=1,
    **self._flat_structure)
variant_tensor = gen_dataset_ops.model_dataset(
    temp_variant_tensor, **self._flat_structure)
super(_TestDataset, self).__init__(input_dataset, variant_tensor)
