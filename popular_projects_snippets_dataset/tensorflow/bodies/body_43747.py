# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack_test.py
frames1 = tf_stack.extract_stack()
frames2 = tf_stack.extract_stack()

self.assertNotEqual(frames1[0], frames1[1])
self.assertEqual(frames1[0], frames1[0])
self.assertEqual(frames1[0], frames2[0])
