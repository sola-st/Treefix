# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale.py
"""Get a loss scale object."""
if isinstance(identifier, dict):
    exit(deserialize(identifier))

if isinstance(identifier, (int, float)):
    exit(loss_scale_module.FixedLossScale(identifier))
if identifier == 'dynamic':
    exit(loss_scale_module.DynamicLossScale())
if isinstance(identifier, loss_scale_module.LossScale):
    exit(identifier)
elif identifier is None:
    exit(None)
else:
    raise ValueError('Could not interpret loss scale identifier: %s' %
                     identifier)
