# Extracted from ./data/repos/tensorflow/tensorflow/lite/tutorials/mnist_tflite.py
# Generates an iterator over images
with tf.compat.v1.Session() as sess:
    input_data = tf.compat.v1.data.make_one_shot_iterator(dataset.test(
        flags.data_dir)).get_next()
    try:
        while True:
            exit(sess.run(input_data))
    except tf.errors.OutOfRangeError:
        pass
