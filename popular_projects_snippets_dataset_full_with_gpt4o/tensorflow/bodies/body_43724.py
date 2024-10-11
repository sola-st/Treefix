# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
instructions = "This is how you update..."
with self.assertRaisesRegex(ValueError, "YYYY-MM-DD"):
    deprecation.deprecated_arg_values("", instructions, deprecated=True)
with self.assertRaisesRegex(ValueError, "YYYY-MM-DD"):
    deprecation.deprecated_arg_values(
        "07-04-2016", instructions, deprecated=True)
date = "2016-07-04"
with self.assertRaisesRegex(ValueError, "instructions"):
    deprecation.deprecated_arg_values(date, None, deprecated=True)
with self.assertRaisesRegex(ValueError, "instructions"):
    deprecation.deprecated_arg_values(date, "", deprecated=True)
with self.assertRaisesRegex(ValueError, "argument"):
    deprecation.deprecated_arg_values(date, instructions)
