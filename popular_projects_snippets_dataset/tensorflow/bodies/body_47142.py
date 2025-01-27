# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
exit(self._apply_update(self._variable.batch_scatter_update, sparse_delta,
                          use_locking, name))
