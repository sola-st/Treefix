import unittest # pragma: no cover

self = type('Mock', (object,), {'_upgrade': lambda self, text: (None, None, None, text.replace('batch_to_space_nd', 'batch_to_space').replace('manip.', '')), 'assertEqual': unittest.TestCase().assertEqual})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
from l3.Runtime import _l_
text = "tf.batch_to_space_nd(input, block_shape, crops, name)"
_l_(21180)
expected_text = "tf.batch_to_space(input, block_shape, crops, name)"
_l_(21181)
_, unused_report, unused_errors, new_text = self._upgrade(text)
_l_(21182)
self.assertEqual(new_text, expected_text)
_l_(21183)

text = "tf.batch_to_space(input, crops, block_size, name)"
_l_(21184)
expected_text = (
    "tf.batch_to_space(input=input, crops=crops, block_shape=block_size, "
    "name=name)")
_l_(21185)
_, unused_report, unused_errors, new_text = self._upgrade(text)
_l_(21186)
self.assertEqual(new_text, expected_text)
_l_(21187)

text = "tf.manip.batch_to_space_nd(input, block_shape, crops, name)"
_l_(21188)
expected_text = "tf.batch_to_space(input, block_shape, crops, name)"
_l_(21189)
_, unused_report, unused_errors, new_text = self._upgrade(text)
_l_(21190)
self.assertEqual(new_text, expected_text)
_l_(21191)
