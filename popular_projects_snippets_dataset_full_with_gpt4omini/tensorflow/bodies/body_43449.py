# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper_test.py
# If set, always load lite module from public API list.
module = MockModule('test')
apis = {'lite': ('', 'cmd')}
module.lite = 5
import cmd as _cmd  # pylint: disable=g-import-not-at-top
wrapped_module = module_wrapper.TFModuleWrapper(
    module, 'test', public_apis=apis, deprecation=False, has_lite=True)
self.assertEqual(wrapped_module.lite, _cmd)
