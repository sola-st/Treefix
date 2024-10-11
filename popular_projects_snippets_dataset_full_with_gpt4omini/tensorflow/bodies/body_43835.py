# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
n1 = type_(n1)
n2 = type_(n2)
with self.assertRaisesRegex(NotImplementedError, 'while/else'):
    tf.function(while_else)(n1, n2)
