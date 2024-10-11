# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
with context.execution_mode(execution_mode):
    device, data_format = device_and_format
    for batch_size in self._train_batch_sizes():
        (images, labels) = resnet50_test_util.random_batch(
            batch_size, data_format)
        model = resnet50.ResNet50(data_format)
        # TODO(b/161911585): tf_to_corert MLIR lowering pipeline should handle
        # case when momentum is not set.
        optimizer = tf.keras.optimizers.SGD(0.1, 0.1)
        apply_grads = apply_gradients
        if defun:
            model.call = tf.function(model.call)
            apply_grads = tf.function(apply_gradients)

        num_burn = 3
        num_iters = 10
        with tf.device(device):
            iterator = make_iterator((images, labels))
            for _ in range(num_burn):
                (images, labels) = iterator.next()
                apply_grads(model, optimizer,
                            compute_gradients(model, images, labels))
            if execution_mode:
                context.async_wait()
            self._force_device_sync()
            gc.collect()

            start = time.time()
            for _ in range(num_iters):
                (images, labels) = iterator.next()
                apply_grads(model, optimizer,
                            compute_gradients(model, images, labels))
            if execution_mode:
                context.async_wait()
            self._force_device_sync()
            self._report(label, start, num_iters, device, batch_size, data_format)
