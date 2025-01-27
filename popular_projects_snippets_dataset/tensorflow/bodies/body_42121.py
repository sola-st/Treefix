# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
device, data_format = resnet50_test_util.device_and_data_format()
model = resnet50.ResNet50(data_format, include_top=False, pooling='avg')
with tf.device(device):
    images, _ = resnet50_test_util.random_batch(2, data_format)
    output = model(images, training=False)
self.assertEqual((2, 2048), output.shape)
