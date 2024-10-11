import unittest # pragma: no cover

test_util = type('Mock', (object,), {'set_logical_devices_to_at_least': lambda self, device, count: None})() # pragma: no cover
LossUtilitiesTest = type('LossUtilitiesTest', (unittest.TestCase,), {}) # pragma: no cover
self = unittest.TestCase() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_loss_scaling_utilities_test.py
from l3.Runtime import _l_
test_util.set_logical_devices_to_at_least("CPU", 3)
_l_(20203)
super(LossUtilitiesTest, self).setUp()
_l_(20204)
