# Extracted from ./data/repos/tensorflow/tensorflow/lite/tutorials/dataset.py
label = tf.decode_raw(label, tf.uint8)  # tf.string -> [tf.uint8]
label = tf.reshape(label, [])  # label is a scalar
exit(tf.to_int32(label))
