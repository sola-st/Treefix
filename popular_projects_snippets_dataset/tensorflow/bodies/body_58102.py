# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
delegate_a = interpreter_wrapper.load_delegate(self._delegate_file)
lib = delegate_a._library

self.assertEqual(lib.get_num_delegates_created(), 1)
self.assertEqual(lib.get_num_delegates_destroyed(), 0)
self.assertEqual(lib.get_num_delegates_invoked(), 0)
self.assertEqual(lib.get_options_counter(), 0)

delegate_b = interpreter_wrapper.load_delegate(
    self._delegate_file, options={
        'unused': False,
        'options_counter': 2
    })
lib = delegate_b._library

self.assertEqual(lib.get_num_delegates_created(), 2)
self.assertEqual(lib.get_num_delegates_destroyed(), 0)
self.assertEqual(lib.get_num_delegates_invoked(), 0)
self.assertEqual(lib.get_options_counter(), 2)

del delegate_a
del delegate_b

self.assertEqual(lib.get_num_delegates_created(), 2)
self.assertEqual(lib.get_num_delegates_destroyed(), 2)
self.assertEqual(lib.get_num_delegates_invoked(), 0)
self.assertEqual(lib.get_options_counter(), 2)
