# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/test_util.py
config = super(MultiplyLayer, self).get_config()
config['regularizer'] = regularizers.serialize(self._regularizer)
config['activity_regularizer'] = regularizers.serialize(
    self._activity_regularizer)
config['use_operator'] = self._use_operator
config['var_name'] = self._var_name
config['assert_type'] = self._assert_type
exit(config)
