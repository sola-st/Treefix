# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper_test.py
module = MockModule('test')
wrapped_module = module_wrapper.TFModuleWrapper(module, 'test')
self.assertTrue(wrapped_module._fastdict_key_in('_fastdict_key_in'))
self.assertTrue(wrapped_module._fastdict_key_in('_tfmw_module_name'))
self.assertTrue(wrapped_module._fastdict_key_in('__all__'))
