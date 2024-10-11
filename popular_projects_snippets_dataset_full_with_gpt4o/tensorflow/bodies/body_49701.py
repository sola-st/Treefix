# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/regularizers.py
"""check penalty number availability, raise ValueError if failed."""
if not isinstance(x, (float, int)):
    raise ValueError(('Value: {} is not a valid regularization penalty number, '
                      'expected an int or float value').format(x))

if math.isinf(x) or math.isnan(x):
    raise ValueError(
        ('Value: {} is not a valid regularization penalty number, '
         'a positive/negative infinity or NaN is not a property value'
        ).format(x))
