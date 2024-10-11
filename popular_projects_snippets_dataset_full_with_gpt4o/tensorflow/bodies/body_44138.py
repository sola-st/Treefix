# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
c = tf.constant(c)
with self.assertRaisesRegex(ValueError, re.compile("'i' is None",
                                                   re.DOTALL)):
    tf.function(target)(c)
