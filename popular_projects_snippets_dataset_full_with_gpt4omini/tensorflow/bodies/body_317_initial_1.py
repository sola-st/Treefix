class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._upgrade = lambda text: (None, [], [], text.replace('batch_to_space_nd', 'batch_to_space')) # pragma: no cover
self.assertEqual = lambda a, b: print('Equal' if a == b else 'Not Equal') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
from l3.Runtime import _l_
text = "tf.batch_to_space_nd(input, block_shape, crops, name)"
_l_(8789)
expected_text = "tf.batch_to_space(input, block_shape, crops, name)"
_l_(8790)
_, unused_report, unused_errors, new_text = self._upgrade(text)
_l_(8791)
self.assertEqual(new_text, expected_text)
_l_(8792)

text = "tf.batch_to_space(input, crops, block_size, name)"
_l_(8793)
expected_text = (
    "tf.batch_to_space(input=input, crops=crops, block_shape=block_size, "
    "name=name)")
_l_(8794)
_, unused_report, unused_errors, new_text = self._upgrade(text)
_l_(8795)
self.assertEqual(new_text, expected_text)
_l_(8796)

text = "tf.manip.batch_to_space_nd(input, block_shape, crops, name)"
_l_(8797)
expected_text = "tf.batch_to_space(input, block_shape, crops, name)"
_l_(8798)
_, unused_report, unused_errors, new_text = self._upgrade(text)
_l_(8799)
self.assertEqual(new_text, expected_text)
_l_(8800)
