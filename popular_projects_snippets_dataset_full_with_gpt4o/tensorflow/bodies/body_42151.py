# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_graph_test.py
with tf.Graph().as_default():
    images = tf.placeholder(tf.float32, image_shape(None))
    model = resnet50.ResNet50(data_format())
    predictions = model(images, training=False)

    init = tf.global_variables_initializer()

    batch_size = 64
    with tf.Session() as sess:
        sess.run(init)
        np_images, _ = random_batch(batch_size)
        num_burn, num_iters = (3, 30)
        for _ in range(num_burn):
            sess.run(predictions, feed_dict={images: np_images})
        start = time.time()
        for _ in range(num_iters):
            # Comparison with the eager execution benchmark in resnet50_test.py
            # isn't entirely fair as the time here includes the cost of copying
            # the feeds from CPU memory to GPU.
            sess.run(predictions, feed_dict={images: np_images})
        self._report('apply', start, num_iters, batch_size)
