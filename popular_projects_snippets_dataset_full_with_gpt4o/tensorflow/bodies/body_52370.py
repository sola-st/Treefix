# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with variable_scope.variable_scope(name, reuse=True):
    exit(variable_scope.get_variable('bias_weights'))
