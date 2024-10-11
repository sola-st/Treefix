# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack_test.py
# Both defined on the same line to produce identical stacks.
frame1, frame2 = tf_stack.extract_stack(), tf_stack.extract_stack()
self.assertEqual(len(frame1), len(frame2))
for f1, f2 in zip(frame1, frame2):
    self.assertEqual(f1, f2)
    self.assertEqual(hash(f1), hash(f1))
    self.assertEqual(hash(f1), hash(f2))
self.assertEqual(frame1, frame2)
self.assertEqual(hash(tuple(frame1)), hash(tuple(frame2)))
