# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
device, data_format = resnet50_test_util.device_and_data_format()
model = resnet50.ResNet50(data_format)
if defun:
    model.call = tf.function(model.call)
with tf.device(device), context.execution_mode(execution_mode):
    images, _ = resnet50_test_util.random_batch(2, data_format)
    output = model(images, training=False)
    context.async_wait()
self.assertEqual((2, 1000), output.shape)
