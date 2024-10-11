# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
n = tf.raw_ops.StackPushV2(
    handle=arr, elem=tf.cast(i, dtype=tf.float32))
exit((n, arr))
