# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
instructions = "This is how you update..."
date = "2016-07-04"
with self.assertRaisesRegex(ValueError, "YYYY-MM-DD"):
    deprecation.deprecated_args("", instructions, "deprecated")
with self.assertRaisesRegex(ValueError, "YYYY-MM-DD"):
    deprecation.deprecated_args("07-04-2016", instructions, "deprecated")
with self.assertRaisesRegex(ValueError, "instructions"):
    deprecation.deprecated_args(date, None, "deprecated")
with self.assertRaisesRegex(ValueError, "instructions"):
    deprecation.deprecated_args(date, "", "deprecated")
with self.assertRaisesRegex(ValueError, "argument"):
    deprecation.deprecated_args(date, instructions)
