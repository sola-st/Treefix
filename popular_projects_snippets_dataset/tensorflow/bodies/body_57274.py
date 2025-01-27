# Extracted from ./data/repos/tensorflow/tensorflow/lite/toco/python/toco_from_protos_test.py
"""Run a couple of TensorFlow graphs against TOCO through the python bin."""
with tf.Session() as sess:
    img = tf.placeholder(name="img", dtype=tf.float32, shape=(1, 64, 64, 3))
    val = img + tf.constant([1., 2., 3.]) + tf.constant([1., 4., 4.])
    out = tf.identity(val, name="out")
    out2 = tf.sin(val, name="out2")
    # This is a valid model
    self._run(sess, img, out, True)
    # This uses an invalid function.
    # TODO(aselle): Check to make sure a warning is included.
    self._run(sess, img, out2, True)
    # This is an identity graph, which doesn't work
    self._run(sess, img, img, False)
