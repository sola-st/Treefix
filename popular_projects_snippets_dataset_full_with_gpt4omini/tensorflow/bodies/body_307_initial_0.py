from typing import List, Tuple, Any # pragma: no cover

class SelfMock: # pragma: no cover
    def _upgrade(self, text: str) -> Tuple[str, Any, List[str], str]: # pragma: no cover
        return text, 'unused_report', [], 'tf.strings.substr(input=input, pos=pos, len=len, name=name, unit=unit)\n' # pragma: no cover
    def assertEqual(self, a: Any, b: Any): # pragma: no cover
        assert a == b, f'Assert failed: {a} != {b}' # pragma: no cover
self = SelfMock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
from l3.Runtime import _l_
text = "tf.substr(input, pos, len, name, unit)\n"
_l_(4602)
_, unused_report, errors, new_text = self._upgrade(text)
_l_(4603)
self.assertEqual("tf.strings.substr(input=input, pos=pos, len=len, "
                 "name=name, unit=unit)\n", new_text)
_l_(4604)
self.assertEqual(errors, [])
_l_(4605)
