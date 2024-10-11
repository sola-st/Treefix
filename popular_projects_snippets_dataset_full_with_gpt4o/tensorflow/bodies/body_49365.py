# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
if is_tensor_or_variable(self.label_weights):
    label_weights = backend.eval(self.label_weights)
else:
    label_weights = self.label_weights
config = {
    'num_thresholds': self.num_thresholds,
    'curve': self.curve.value,
    'summation_method': self.summation_method.value,
    # We remove the endpoint thresholds as an inverse of how the thresholds
    # were initialized. This ensures that a metric initialized from this
    # config has the same thresholds.
    'thresholds': self.thresholds[1:-1],
    'multi_label': self.multi_label,
    'label_weights': label_weights
}
base_config = super(AUC, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
