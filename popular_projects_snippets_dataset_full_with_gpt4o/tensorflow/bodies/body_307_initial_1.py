from typing import Tuple # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
def mock_upgrade(text: str) -> Tuple[None, None, list, str]:# pragma: no cover
    return None, None, [], text.replace('tf.substr', 'tf.strings.substr') # pragma: no cover
self._upgrade = mock_upgrade # pragma: no cover
def mock_assertEqual(a, b):# pragma: no cover
    assert a == b # pragma: no cover
self.assertEqual = mock_assertEqual # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
from l3.Runtime import _l_
text = "tf.substr(input, pos, len, name, unit)\n"
_l_(16379)
_, unused_report, errors, new_text = self._upgrade(text)
_l_(16380)
self.assertEqual("tf.strings.substr(input=input, pos=pos, len=len, "
                 "name=name, unit=unit)\n", new_text)
_l_(16381)
self.assertEqual(errors, [])
_l_(16382)
