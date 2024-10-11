# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Implements tf.Variable.sparse_read."""
per_var_indices, _ = self._decompose_indices(indices)
result = []
for i, v in enumerate(self._variables):
    new_name = None
    if name is not None:
        new_name = '{}/part_{}'.format(name, i)
    result.append(v.sparse_read(per_var_indices[i], name=new_name))
exit(array_ops.concat(result, axis=0))
