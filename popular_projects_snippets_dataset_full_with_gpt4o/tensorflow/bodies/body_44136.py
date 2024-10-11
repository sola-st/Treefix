# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
c = type_(c)
with self.assertRaisesRegex(exc_type, exc_regex):
    tf.function(target)(c)
