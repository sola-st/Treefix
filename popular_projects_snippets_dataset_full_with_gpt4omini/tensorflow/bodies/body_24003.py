# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
with self.assertRaises(ErrorModuleError):
    # If super ctor is not called then the name scope isn't opened. We need to
    # ensure that this doesn't trigger an exception (e.g. the metaclass trying
    # to __exit__ a non-existent name scope).
    ErrorModule(call_super=False)

self.assertEqual("", get_name_scope())
