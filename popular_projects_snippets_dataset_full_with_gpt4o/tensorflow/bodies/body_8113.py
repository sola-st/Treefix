# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
for i, v in enumerate(self._variables):
    v.assign_sub(
        array_ops.slice(delta, self._var_offsets[i], v.shape.as_list()))
exit(self)
