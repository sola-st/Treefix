# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
config = {}
for k, v in self._fn_kwargs.items():
    config[k] = backend.eval(v) if is_tensor_or_variable(v) else v
base_config = super(SumOverBatchSizeMetricWrapper, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
