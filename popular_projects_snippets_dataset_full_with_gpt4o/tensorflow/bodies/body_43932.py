# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
exit(tf.data.Dataset.range(n).map(lambda x: tf.cast(x, tf.int32)))
