# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_graph_test.py
# Use small batches for tests because the OSS version runs
# in constrained GPU environment with 1-2GB of memory.
batch_size = 8
with tf.Graph().as_default():
    images = tf.placeholder(tf.float32, image_shape(None))
    model = resnet50.ResNet50(data_format())
    predictions = model(images, training=False)

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        np_images, _ = random_batch(batch_size)
        out = sess.run(predictions, feed_dict={images: np_images})
        self.assertAllEqual([batch_size, 1000], out.shape)
