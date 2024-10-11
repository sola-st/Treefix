# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = ErrorModule(call_super=True, raise_in_constructor=False)
with self.assertRaises(ErrorModuleError):
    mod()

self.assertEqual("", get_name_scope())
