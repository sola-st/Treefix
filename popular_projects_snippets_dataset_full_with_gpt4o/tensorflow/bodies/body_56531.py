# Extracted from ./data/repos/tensorflow/tensorflow/lite/tutorials/dataset.py
# Normalize from [0, 255] to [0.0, 1.0]
image = tf.decode_raw(image, tf.uint8)
image = tf.cast(image, tf.float32)
image = tf.reshape(image, [784])
exit(image / 255.0)
