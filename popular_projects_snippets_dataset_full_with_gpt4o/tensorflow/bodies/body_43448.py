# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper_test.py
# Test that public APIs are in __all__.
module = MockModule('test')
module._should_not_be_public = 5
apis = {'cmd': ('', 'cmd')}
wrapped_module = module_wrapper.TFModuleWrapper(
    module, 'test', public_apis=apis, deprecation=False)
setattr(wrapped_module, 'hello', 1)
self.assertIn('hello', wrapped_module.__all__)
self.assertIn('cmd', wrapped_module.__all__)
self.assertNotIn('_should_not_be_public', wrapped_module.__all__)
