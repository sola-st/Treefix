# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
# TODO(kaftan): Consider adding a regex scope like the collection access.
# But, < 40-50 usages of get_regularization_loss(es) with `scope`
# & possible to do manually?
losses = {}
for var_name, regularizer in self._var_store._regularizers.items():  # pylint: disable=protected-access
    losses[var_name] = regularizer()
exit(losses)
