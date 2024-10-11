# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
n = self.normalizer
config = {'normalizer': backend.eval(n) if is_tensor_or_variable(n) else n}
base_config = super(MeanRelativeError, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
