# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
strat, ds = _distributed_dataset()
with self.assertRaises(tf.errors.OutOfRangeError):
    tf.function(test_fn)(strat, ds, tf.constant(True))
