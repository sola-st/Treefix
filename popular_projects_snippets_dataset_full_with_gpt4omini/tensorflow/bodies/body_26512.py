# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/cardinality.py
self._input_dataset = input_dataset
self._expected_cardinality = ops.convert_to_tensor(
    expected_cardinality, dtype=dtypes.int64, name="expected_cardinality")

# pylint: enable=protected-access
variant_tensor = ged_ops.assert_cardinality_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._expected_cardinality,
    **self._flat_structure)
super(_AssertCardinalityDataset, self).__init__(input_dataset,
                                                variant_tensor)
