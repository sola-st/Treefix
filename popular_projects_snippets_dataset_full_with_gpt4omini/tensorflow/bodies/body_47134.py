# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
exit(self._apply_assign_update(self._variable.assign_sub, delta,
                                 use_locking, name, read_value))
