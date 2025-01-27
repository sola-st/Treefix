# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
quarantine.add_function_callback(lambda f: None)
quarantine.add_function_callback(lambda f: None)
self.assertLen(monomorphic_function._function_callbacks, 2)
quarantine.clear_function_callbacks()
self.assertEmpty(monomorphic_function._function_callbacks)  # pylint:disable=protected-access
