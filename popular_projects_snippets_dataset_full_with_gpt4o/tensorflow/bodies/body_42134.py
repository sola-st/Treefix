# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
with context.execution_mode(execution_mode):
    device, data_format = device_and_format
    model = resnet50.ResNet50(data_format)
    if defun:
        model.call = tf.function(model.call)
    batch_size = 64
    num_burn = 5
    num_iters = 30
    with tf.device(device):
        images, _ = resnet50_test_util.random_batch(batch_size, data_format)
        for _ in range(num_burn):
            model(images, training=False).cpu()
        if execution_mode:
            context.async_wait()
        gc.collect()
        start = time.time()
        for _ in range(num_iters):
            model(images, training=False).cpu()
        if execution_mode:
            context.async_wait()
        self._report(label, start, num_iters, device, batch_size, data_format)
