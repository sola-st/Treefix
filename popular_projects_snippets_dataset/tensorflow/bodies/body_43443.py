# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper_test.py
module = MockModule('test')
wrapped_module = module_wrapper.TFModuleWrapper(module, 'test')
self.assertTrue(tf_inspect.ismodule(wrapped_module))
