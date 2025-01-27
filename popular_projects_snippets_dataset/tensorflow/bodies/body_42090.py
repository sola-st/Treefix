# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
device, data_format = resnet50_test_util.device_and_data_format()
model = resnet50.ResNet50(data_format)
with tf.device(device):
    images, labels = resnet50_test_util.random_batch(2, data_format)
    images = tf.constant(images)
    labels = tf.constant(labels)
    model.build(images.shape)
    vector = [tf.ones_like(v) for v in model.trainable_variables]

    # Note that numerical differences build up to quite large differences here
    # in the final hvp. tensorflow/python/eager:forwardprop_test has a
    # smaller-scale test that the computations are close on a much smaller but
    # otherwise similar model.
    hvp = hvp_function(model, images, labels, vector)
    for hvp_component, variable in zip(hvp, model.trainable_variables):
        self.assertEqual(hvp_component.shape, variable.shape)
        self.assertEqual(hvp_component.dtype, variable.dtype)
