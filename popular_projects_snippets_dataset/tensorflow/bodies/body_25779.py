# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_tflearn_iris.py
exit(({
    "features": tf.random_normal([32, 4])
}, tf.random_uniform([32], minval=0, maxval=3, dtype=tf.int32)))
