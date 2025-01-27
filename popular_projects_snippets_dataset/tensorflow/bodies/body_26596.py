# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/testing.py
"""See `non_serializable()` for details."""
self._input_dataset = input_dataset
variant_tensor = (
    gen_experimental_dataset_ops.experimental_non_serializable_dataset(
        self._input_dataset._variant_tensor,  # pylint: disable=protected-access
        **self._flat_structure))
super(_NonSerializableDataset, self).__init__(input_dataset, variant_tensor)
