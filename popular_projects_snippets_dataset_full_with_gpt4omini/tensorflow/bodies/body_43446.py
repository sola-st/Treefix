# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper_test.py
# Test that we can override and add fields to the wrapped module.
module = MockModule('test')
apis = {'cmd': ('', 'cmd')}
wrapped_module = module_wrapper.TFModuleWrapper(
    module, 'test', public_apis=apis, deprecation=False)
import cmd as _cmd  # pylint: disable=g-import-not-at-top
self.assertEqual(wrapped_module.cmd, _cmd)
setattr(wrapped_module, 'cmd', 1)
setattr(wrapped_module, 'cgi', 2)
self.assertEqual(wrapped_module.cmd, 1)  # override
# Verify that the values are also updated in the cache
# of the FastModuleType object
self.assertEqual(wrapped_module._fastdict_get('cmd'), 1)
self.assertEqual(wrapped_module.cgi, 2)  # add
self.assertEqual(wrapped_module._fastdict_get('cgi'), 2)
