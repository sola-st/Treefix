# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
exit(ShardedVariableSpec(
    *(resource_variable_ops.VariableSpec(v.shape, v.dtype)
      for v in self._variables)))
