# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
l1 = type_(l1)
l2 = type_(l2)
with self.assertRaisesRegex(NotImplementedError, 'for/else'):
    tf.function(for_else)(l1, l2)
