# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper_test.py
name = PickleTest.__module__  # The current module is a submodule.
module = module_wrapper.TFModuleWrapper(MockModule(name), name)
restored = pickle.loads(pickle.dumps(module))
self.assertEqual(restored.__name__, name)
self.assertIsNotNone(restored.PickleTest)
