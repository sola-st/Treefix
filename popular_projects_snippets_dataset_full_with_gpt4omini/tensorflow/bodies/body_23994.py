# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = PropertyThrowsWhenCalledModule()
with self.assertRaises(AssertionError):
    mod.raise_assertion_error  # pylint: disable=pointless-statement
