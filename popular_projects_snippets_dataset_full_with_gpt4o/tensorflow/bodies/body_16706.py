# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Create a variable store."""
self._vars = {}  # A dictionary of the stored TensorFlow variables.
self._partitioned_vars = {}  # A dict of the stored PartitionedVariables.
self._store_eager_variables = False
