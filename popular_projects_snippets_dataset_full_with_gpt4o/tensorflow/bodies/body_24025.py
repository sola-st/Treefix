# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = ModuleWithFunctionAnnotatedCall()
self.assertIsInstance(mod.forward, def_function.Function)
self.assertIsInstance(mod.forward_ag, def_function.Function)
