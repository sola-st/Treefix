# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Sets sample weight attribute on the model."""
# List with the same length as model outputs.
if sample_weights is not None:
    if len(sample_weights) != len(self._training_endpoints):
        raise ValueError('Provided sample weights must have same length as the '
                         'number of outputs. Expected: {}, got: {}.'.format(
                             len(self._training_endpoints),
                             len(sample_weights)))
else:
    sample_weights = [None] * len(self._training_endpoints)
for endpoint, weight in zip(self._training_endpoints, sample_weights):
    endpoint.populate_sample_weight(weight, endpoint.sample_weight_mode)
