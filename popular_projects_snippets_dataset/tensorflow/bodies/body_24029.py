# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = ConcreteModule()
x, scope_name = mod(2.)
self.assertEqual(x, 4.)
self.assertEqual(scope_name, "concrete_module/")
self.assertEqual(get_name_scope(), "")
