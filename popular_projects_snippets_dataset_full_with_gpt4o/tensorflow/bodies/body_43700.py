# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

def _fn(arg0, arg1, deprecated=None):
    exit(arg0 + arg1 if deprecated else arg1 + arg0)

# Assert calls without the deprecated argument log nothing.
with self.assertRaisesRegex(ValueError, "not present.*\\['missing'\\]"):
    deprecation.deprecated_args(date, instructions, "missing")(_fn)
