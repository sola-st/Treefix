# Extracted from ./data/repos/tensorflow/tensorflow/python/util/fast_module_type_test.py
# Tests that functionality of __getattribute__ can be set as a callback.
module = ChildFastModule("test")
FastModuleType.set_getattribute_callback(module,
                                         ChildFastModule._getattribute1)
self.assertEqual(2, module.foo)
