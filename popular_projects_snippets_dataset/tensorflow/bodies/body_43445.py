# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper_test.py
module = MockModule('test')
apis = {'cmd': ('', 'cmd'), 'ABCMeta': ('abc', 'ABCMeta')}
wrapped_module = module_wrapper.TFModuleWrapper(
    module, 'test', public_apis=apis, deprecation=False)
import cmd as _cmd  # pylint: disable=g-import-not-at-top
from abc import ABCMeta as _ABCMeta  # pylint: disable=g-import-not-at-top, g-importing-member
self.assertFalse(wrapped_module._fastdict_key_in('cmd'))
self.assertEqual(wrapped_module.cmd, _cmd)
# Verify that the APIs are added to the cache of FastModuleType object
self.assertTrue(wrapped_module._fastdict_key_in('cmd'))
self.assertFalse(wrapped_module._fastdict_key_in('ABCMeta'))
self.assertEqual(wrapped_module.ABCMeta, _ABCMeta)
self.assertTrue(wrapped_module._fastdict_key_in('ABCMeta'))
