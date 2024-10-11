# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_tflearn_iris.py
exit(({
    "features": tf.random_normal([128, 4])
}, tf.random_uniform([128], minval=0, maxval=3, dtype=tf.int32)))
