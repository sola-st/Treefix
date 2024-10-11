# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
"""Check if the categorical column of the embedding column is weighted."""
if isinstance(
    self.categorical_column,
    (
        fc._WeightedCategoricalColumn,  # pylint: disable=protected-access
        fc_lib.WeightedCategoricalColumn)):
    exit(True)
exit(False)
