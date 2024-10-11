# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/regularizers.py
l1 = kwargs.pop('l', l1)  # Backwards compatibility
if kwargs:
    raise TypeError('Argument(s) not recognized: %s' % (kwargs,))

l1 = 0.01 if l1 is None else l1
_check_penalty_number(l1)

self.l1 = backend.cast_to_floatx(l1)
