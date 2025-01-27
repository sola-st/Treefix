# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
config = {'num_thresholds': self.num_thresholds, 'recall': self.recall}
base_config = super(PrecisionAtRecall, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
