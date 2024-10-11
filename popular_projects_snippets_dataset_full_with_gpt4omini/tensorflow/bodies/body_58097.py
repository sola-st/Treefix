# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
"""Tests the delegate creation and destruction."""
interpreter = self._TestInterpreter(model_path=self._model_file)
lib = interpreter._delegates[0]._library

self.assertEqual(lib.get_num_delegates_created(), 1)
self.assertEqual(lib.get_num_delegates_destroyed(), 0)
self.assertEqual(lib.get_num_delegates_invoked(), 1)

del interpreter

self.assertEqual(lib.get_num_delegates_created(), 1)
self.assertEqual(lib.get_num_delegates_destroyed(), 1)
self.assertEqual(lib.get_num_delegates_invoked(), 1)
