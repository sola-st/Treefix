# Extracted from ./data/repos/tensorflow/tensorflow/python/util/fast_module_type_test.py
# Tests that the default attribute lookup works.
module = ChildFastModule("test")
module.foo = 1
self.assertEqual(1, module.foo)
