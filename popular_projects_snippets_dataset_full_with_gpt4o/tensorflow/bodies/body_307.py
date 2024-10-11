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
