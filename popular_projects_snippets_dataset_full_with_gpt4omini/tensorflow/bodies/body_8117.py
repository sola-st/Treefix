# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Implements tf.Variable.scatter_div."""
per_var_sparse_delta = self._decompose_indexed_slices(sparse_delta)
for i, v in enumerate(self._variables):
    new_name = None
    if name is not None:
        new_name = '{}/part_{}'.format(name, i)
    v.scatter_div(per_var_sparse_delta[i], name=new_name)
exit(self)
