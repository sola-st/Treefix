# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
delegate = interpreter_wrapper.load_delegate(self._delegate_file)
lib = delegate._library

self.assertEqual(lib.get_num_delegates_created(), 1)
self.assertEqual(lib.get_num_delegates_destroyed(), 0)
self.assertEqual(lib.get_num_delegates_invoked(), 0)

interpreter_a = interpreter_wrapper.Interpreter(
    model_path=self._model_file, experimental_delegates=[delegate])

self.assertEqual(lib.get_num_delegates_created(), 1)
self.assertEqual(lib.get_num_delegates_destroyed(), 0)
self.assertEqual(lib.get_num_delegates_invoked(), 1)

interpreter_b = interpreter_wrapper.Interpreter(
    model_path=self._model_file, experimental_delegates=[delegate])

self.assertEqual(lib.get_num_delegates_created(), 1)
self.assertEqual(lib.get_num_delegates_destroyed(), 0)
self.assertEqual(lib.get_num_delegates_invoked(), 2)

del delegate
del interpreter_a

self.assertEqual(lib.get_num_delegates_created(), 1)
self.assertEqual(lib.get_num_delegates_destroyed(), 0)
self.assertEqual(lib.get_num_delegates_invoked(), 2)

del interpreter_b

self.assertEqual(lib.get_num_delegates_created(), 1)
self.assertEqual(lib.get_num_delegates_destroyed(), 1)
self.assertEqual(lib.get_num_delegates_invoked(), 2)
