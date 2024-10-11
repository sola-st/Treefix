# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
old_symbol = "tf.conj(a)"
new_symbol = "tf.math.conj(a)"

import_header = "import tensorflow as tf\n"
text = import_header + old_symbol
expected_text = "import tensorflow.compat.v2 as tf\n" + new_symbol
_, unused_report, unused_errors, new_text = self._upgrade(
    text, import_rename=True)
self.assertEqual(new_text, expected_text)

import_header = "import tensorflow as tf, other_import as y\n"
text = import_header + old_symbol
new_import_header = "import tensorflow.compat.v2 as tf, other_import as y\n"
expected_text = new_import_header + new_symbol
_, unused_report, unused_errors, new_text = self._upgrade(
    text, import_rename=True)
self.assertEqual(new_text, expected_text)

import_header = ("import tensorflow as tf\n"
                 "import tensorflow.compat.v1 as tf_v1\n"
                 "import tensorflow.compat.v2 as tf_v2\n")
text = import_header + old_symbol
expected_header = ("import tensorflow.compat.v2 as tf\n"
                   "import tensorflow.compat.v1 as tf_v1\n"
                   "import tensorflow.compat.v2 as tf_v2\n")
expected_text = expected_header + new_symbol
_, _, _, new_text = self._upgrade(text, import_rename=True)
self.assertEqual(new_text, expected_text)

import_header = ("import tensorflow.compat.v1 as tf\n"
                 "import tensorflow.compat.v1 as tf_v1\n"
                 "import tensorflow.compat.v2 as tf_v2\n")
text = import_header + old_symbol
expected_header = ("import tensorflow.compat.v2 as tf\n"
                   "import tensorflow.compat.v1 as tf_v1\n"
                   "import tensorflow.compat.v2 as tf_v2\n")
expected_text = expected_header + new_symbol
_, _, _, new_text = self._upgrade(
    text, import_rename=True, upgrade_compat_v1_import=True)
self.assertEqual(new_text, expected_text)

import_header = ("import tensorflow.compat.v1 as tf\n"
                 "import tensorflow.compat.v1 as tf_v1\n"
                 "import tensorflow.compat.v2 as tf_v2\n")
text = import_header + old_symbol
expected_header = ("import tensorflow as tf\n"
                   "import tensorflow.compat.v1 as tf_v1\n"
                   "import tensorflow.compat.v2 as tf_v2\n")
expected_text = expected_header + new_symbol
_, _, _, new_text = self._upgrade(
    text, import_rename=False, upgrade_compat_v1_import=True)
self.assertEqual(new_text, expected_text)

import_header = "from tensorflow import foo\n"
text = import_header + old_symbol
expected_text = "from tensorflow.compat.v2 import foo\n" + new_symbol
_, unused_report, unused_errors, new_text = self._upgrade(
    text, import_rename=True)
self.assertEqual(new_text, expected_text)

import_header = "from tensorflow import *\n"
text = import_header + old_symbol
expected_text = "from tensorflow.compat.v2 import *\n" + new_symbol
_, unused_report, unused_errors, new_text = self._upgrade(
    text, import_rename=True)
self.assertEqual(new_text, expected_text)

import_header = "from tensorflow.foo import bar\n"
text = import_header + old_symbol
expected_text = "from tensorflow.compat.v2.foo import bar\n" + new_symbol
_, unused_report, unused_errors, new_text = self._upgrade(
    text, import_rename=True)
self.assertEqual(new_text, expected_text)

import_header = ("from tensorflow import foo as tf\n"
                 "from tensorflow.compat import v1 as tf_v1\n"
                 "from tensorflow.compat import v2 as tf_v2\n")
text = import_header + old_symbol
expected_header = ("from tensorflow.compat.v2 import foo as tf\n"
                   "from tensorflow.compat import v1 as tf_v1\n"
                   "from tensorflow.compat import v2 as tf_v2\n")
expected_text = expected_header + new_symbol
_, _, _, new_text = self._upgrade(text, import_rename=True)
self.assertEqual(new_text, expected_text)
