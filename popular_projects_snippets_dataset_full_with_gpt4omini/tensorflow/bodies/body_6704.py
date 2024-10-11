# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
exit(self._scatter_xxx(gen_resource_variable_ops.resource_scatter_sub,
                         "scatter_sub", var, sparse_delta, use_locking,
                         name))
