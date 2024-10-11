# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/datasets_test.py
# This is for the same reason why returns in loops aren't allowed.
# TODO(mdan): This might be resolved by unrolling the loop once.
with self.assertRaisesRegex(
    NotImplementedError,
    'a return statement cannot be placed inside this TensorFlow loop'):
    tf.function(iterator_loop_with_return)(self.ds)
