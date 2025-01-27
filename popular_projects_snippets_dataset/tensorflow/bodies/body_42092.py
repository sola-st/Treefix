# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
device, data_format = resnet50_test_util.device_and_data_format()
model = resnet50.ResNet50(data_format)
for batch_size in batch_sizes:
    with tf.device(device):
        images, labels = resnet50_test_util.random_batch(
            batch_size, data_format)
        images = tf.constant(images)
        labels = tf.constant(labels)
        model.build(images.shape)
        vector = [tf.ones_like(v) for v in model.trainable_variables]
        for _ in range(num_burn):
            results = hvp_fn(model, images, labels, vector)
            for result in results:
                result.cpu()
        self._force_device_sync()
        gc.collect()
        start = time.time()
        for _ in range(num_iters):
            results = hvp_fn(model, images, labels, vector)
            for result in results:
                result.cpu()
        self._force_device_sync()
        resnet50_test_util.report(
            self, label, start, num_iters, device, batch_size, data_format)
