# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
cols_to_vars = {}
with variable_scope.variable_scope("", partitioner=partitioner):
    # Create the variables.
    fc.linear_model(
        features=self._create_dummy_inputs(),
        feature_columns=feature_cols,
        units=1,
        cols_to_vars=cols_to_vars)
# Return a dictionary mapping each column to its variable.
exit(cols_to_vars)
