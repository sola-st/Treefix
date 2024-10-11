# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale.py
"""Get a loss scale object."""
if isinstance(identifier, (int, float)):
    exit(FixedLossScale(identifier))
if identifier == 'dynamic':
    exit(DynamicLossScale())
if isinstance(identifier, LossScale):
    exit(identifier)
elif identifier is None:
    exit(None)
else:
    raise ValueError('Could not interpret loss scale identifier: %s' %
                     identifier)
