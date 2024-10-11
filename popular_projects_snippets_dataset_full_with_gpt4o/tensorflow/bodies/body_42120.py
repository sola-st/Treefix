# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
device, data_format = resnet50_test_util.device_and_data_format()
model = resnet50.ResNet50(data_format, include_top=False)
with tf.device(device):
    images, _ = resnet50_test_util.random_batch(2, data_format)
    output = model(images, training=False)
output_shape = ((2, 2048, 1, 1)
                if data_format == 'channels_first' else (2, 1, 1, 2048))
self.assertEqual(output_shape, output.shape)
