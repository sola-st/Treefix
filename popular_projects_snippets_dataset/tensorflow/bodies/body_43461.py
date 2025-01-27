# Extracted from ./data/repos/tensorflow/tensorflow/python/util/fast_module_type_test.py
# Tests that functionality of __getattr__ can be set as a callback.
module = ChildFastModule("test")
FastModuleType.set_getattribute_callback(module,
                                         ChildFastModule._getattribute2)
FastModuleType.set_getattr_callback(module, ChildFastModule._getattr)
self.assertEqual(3, module.foo)
