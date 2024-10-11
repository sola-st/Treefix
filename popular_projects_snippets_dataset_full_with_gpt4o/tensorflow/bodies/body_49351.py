# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
config = {
    'num_thresholds': self.num_thresholds,
    'sensitivity': self.sensitivity
}
base_config = super(SpecificityAtSensitivity, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
