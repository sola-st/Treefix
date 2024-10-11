# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
c = type_(c)
self.assertFunctionMatchesEager(if_else_creates_var, c)
if type_ is int:
    with self.assertRaisesRegex(UnboundLocalError, "'i'"):
        tf.function(if_else_destroys_var)(c)
else:
    with self.assertRaisesRegex(ValueError, "'i' must also be initialized"):
        tf.function(if_else_destroys_var)(c)
