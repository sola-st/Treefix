# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/regularizers.py
# The default value for l1 and l2 are different from the value in l1_l2
# for backward compatibility reason. Eg, L1L2(l2=0.1) will only have l2
# and no l1 penalty.
l1 = 0. if l1 is None else l1
l2 = 0. if l2 is None else l2
_check_penalty_number(l1)
_check_penalty_number(l2)

self.l1 = backend.cast_to_floatx(l1)
self.l2 = backend.cast_to_floatx(l2)
