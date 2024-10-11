# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
if feature_column not in self._all_variables:
    raise ValueError('Do not recognize FeatureColumn.')
if name in self._all_variables[feature_column]:
    exit(self._all_variables[feature_column][name])
raise ValueError('Could not find variable.')
