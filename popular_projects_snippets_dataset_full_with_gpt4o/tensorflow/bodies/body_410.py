# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
old_symbol = "tf.conj(a)"
new_symbol = "tf.math.conj(a)"

# We upgrade the base un-versioned tensorflow aliased as tf
import_header = "import tensorflow as tf\n"
text = import_header + old_symbol
expected_text = import_header + new_symbol
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

import_header = ("import tensorflow as tf\n"
                 "import tensorflow.compat.v1 as tf_v1\n"
                 "import tensorflow.compat.v2 as tf_v2\n")
text = import_header + old_symbol
expected_text = import_header + new_symbol
_, _, _, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

# We don't handle unaliased tensorflow imports currently,
# So the upgrade script show log errors
import_header = "import tensorflow\n"
text = import_header + old_symbol
expected_text = import_header + old_symbol
_, _, errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
self.assertIn("unaliased `import tensorflow`", "\n".join(errors))

# Upgrading explicitly-versioned tf code is unsafe, but we don't
# need to throw errors when we detect explicitly-versioned tf.
import_header = "import tensorflow.compat.v1 as tf\n"
text = import_header + old_symbol
expected_text = import_header + old_symbol
_, report, errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
self.assertIn("`tensorflow.compat.v1` was directly imported as `tf`",
              report)
self.assertEmpty(errors)

import_header = "from tensorflow.compat import v1 as tf\n"
text = import_header + old_symbol
expected_text = import_header + old_symbol
_, report, errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
self.assertIn("`tensorflow.compat.v1` was directly imported as `tf`",
              report)
self.assertEmpty(errors)

import_header = "from tensorflow.compat import v1 as tf, v2 as tf2\n"
text = import_header + old_symbol
expected_text = import_header + old_symbol
_, report, errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
self.assertIn("`tensorflow.compat.v1` was directly imported as `tf`",
              report)
self.assertEmpty(errors)

import_header = "import tensorflow.compat.v2 as tf\n"
text = import_header + old_symbol
expected_text = import_header + old_symbol
_, report, errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
self.assertIn("`tensorflow.compat.v2` was directly imported as `tf`",
              report)
self.assertEmpty(errors)

import_header = "from tensorflow.compat import v1 as tf1, v2 as tf\n"
text = import_header + old_symbol
expected_text = import_header + old_symbol
_, report, errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
self.assertIn("`tensorflow.compat.v2` was directly imported as `tf`",
              report)
self.assertEmpty(errors)
