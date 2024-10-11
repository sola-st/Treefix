# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
exit(tf.cond(
    b, true_fn=lambda: true_fn(x), false_fn=lambda: false_fn(x)))
