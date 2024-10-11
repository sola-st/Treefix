# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
instructions = "This is how you update..."
with self.assertRaisesRegex(ValueError, "YYYY-MM-DD"):
    deprecation.deprecated("", instructions)
with self.assertRaisesRegex(ValueError, "YYYY-MM-DD"):
    deprecation.deprecated("07-04-2016", instructions)
date = "2016-07-04"
with self.assertRaisesRegex(ValueError, "instructions"):
    deprecation.deprecated(date, None)
with self.assertRaisesRegex(ValueError, "instructions"):
    deprecation.deprecated(date, "")
