# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
"""Populates both id_tensor and weight_tensor."""
ids_and_weights = inputs.get(self)
exit(fc.CategoricalColumn.IdWeightPair(
    id_tensor=ids_and_weights[0], weight_tensor=ids_and_weights[1]))
