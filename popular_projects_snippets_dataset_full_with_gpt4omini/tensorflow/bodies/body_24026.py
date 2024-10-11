# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = ModuleWithFunctionAnnotatedCall()
self.assertEqual(self.evaluate(mod.forward()),
                 b"module_with_function_annotated_call/")
self.assertEqual(self.evaluate(mod.forward_ag()),
                 b"module_with_function_annotated_call/")
