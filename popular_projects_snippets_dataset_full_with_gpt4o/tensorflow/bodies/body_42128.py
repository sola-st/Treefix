# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
device, data_format = resnet50_test_util.device_and_data_format()
model = resnet50.ResNet50(data_format)
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.1)
with tf.device(device):
    images, labels = resnet50_test_util.random_batch(2, data_format)
    gc.disable()
    # Warm up. Note that this first run does create significant amounts of
    # garbage to be collected. The hope is that this is a build-only effect,
    # and a subsequent training loop will create nothing which needs to be
    # collected.
    apply_gradients(model, optimizer,
                    compute_gradients(model, images, labels))
    gc.collect()
    previous_gc_debug_flags = gc.get_debug()
    gc.set_debug(gc.DEBUG_SAVEALL)
    for _ in range(2):
        # Run twice to ensure that garbage that is created on the first
        # iteration is no longer accessible.
        apply_gradients(model, optimizer,
                        compute_gradients(model, images, labels))
    gc.collect()
    # There should be no garbage requiring collection.
    self.assertEqual(0, len(gc.garbage))
    gc.set_debug(previous_gc_debug_flags)
    gc.enable()
