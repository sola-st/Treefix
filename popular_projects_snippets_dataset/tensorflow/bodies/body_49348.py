# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
config = {
    'num_thresholds': self.num_thresholds,
    'specificity': self.specificity
}
base_config = super(SensitivityAtSpecificity, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
