# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
config = {'num_thresholds': self.num_thresholds,
          'precision': self.precision}
base_config = super(RecallAtPrecision, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
