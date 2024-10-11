# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/regularizers.py
l2 = kwargs.pop('l', l2)  # Backwards compatibility
if kwargs:
    raise TypeError('Argument(s) not recognized: %s' % (kwargs,))

l2 = 0.01 if l2 is None else l2
_check_penalty_number(l2)

self.l2 = backend.cast_to_floatx(l2)
