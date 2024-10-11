# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper_test.py
# Test that we can override and add fields to the wrapped module.
module = MockModule('test')
apis = {'cmd': ('', 'cmd')}
wrapped_module = module_wrapper.TFModuleWrapper(
    module, 'test', public_apis=apis, deprecation=False)
import cmd as _cmd  # pylint: disable=g-import-not-at-top
# At first cmd key does not exist in __dict__
self.assertNotIn('cmd', wrapped_module.__dict__)
# After it is referred (lazyloaded), it gets added to __dict__
wrapped_module.cmd  # pylint: disable=pointless-statement
self.assertEqual(wrapped_module.__dict__['cmd'], _cmd)
# When we call setattr, it also gets added to __dict__
setattr(wrapped_module, 'cmd2', _cmd)
self.assertEqual(wrapped_module.__dict__['cmd2'], _cmd)
