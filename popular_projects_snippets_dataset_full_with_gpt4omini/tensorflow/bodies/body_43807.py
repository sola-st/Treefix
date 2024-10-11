# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/datasets_test.py
# Graph ops raise OutOfRangeError, but eager ops raise StopIteration
with self.assertRaises(tf.errors.OutOfRangeError):
    tf.function(iterator_next_with_catching_stop_iteration)(
        self.ds, tf.constant(True))
