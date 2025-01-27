# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
config = {}

if type(self) is MeanMetricWrapper:  # pylint: disable=unidiomatic-typecheck
    # Only include function argument when the object is a MeanMetricWrapper
    # and not a subclass.
    config['fn'] = self._fn

for k, v in self._fn_kwargs.items():
    config[k] = backend.eval(v) if is_tensor_or_variable(v) else v
base_config = super(MeanMetricWrapper, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
