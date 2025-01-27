# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
expected_stack = inspect.stack()
actual_stack = tf_inspect.stack()
self.assertEqual(len(expected_stack), len(actual_stack))
self.assertEqual(expected_stack[0][0], actual_stack[0][0])  # Frame object
self.assertEqual(expected_stack[0][1], actual_stack[0][1])  # Filename
self.assertEqual(expected_stack[0][2],
                 actual_stack[0][2] - 1)  # Line number
self.assertEqual(expected_stack[0][3], actual_stack[0][3])  # Function name
self.assertEqual(expected_stack[1:], actual_stack[1:])
