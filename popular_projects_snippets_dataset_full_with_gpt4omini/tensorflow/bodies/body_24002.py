# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
with self.assertRaises(ErrorModuleError):
    # If super constructor is called then a name scope is opened then an error
    # is thrown. The metaclass should handle this and close the namescope
    # before re-throwing the exception.
    ErrorModule(call_super=True)

self.assertEqual("", get_name_scope())
