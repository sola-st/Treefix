# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = ModuleWithFunctionAnnotatedCall()
self.assertEqual(self.evaluate(mod.forward.get_concrete_function()()),
                 b"module_with_function_annotated_call/")
self.assertEqual(self.evaluate(mod.forward_ag.get_concrete_function()()),
                 b"module_with_function_annotated_call/")
