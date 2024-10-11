# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
config = {'class_id': self.class_id}
base_config = super(SensitivitySpecificityBase, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
