# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
config = {'thresholds': self.init_thresholds}
base_config = super(_ConfusionMatrixConditionCount, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
