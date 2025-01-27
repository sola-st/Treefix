# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
device, data_format = resnet50_test_util.device_and_data_format()
model = resnet50.ResNet50(
    data_format, block3_strides=True, include_top=False)
intermediates_dict = {}
with tf.device(device):
    images, _ = resnet50_test_util.random_batch(2, data_format)
    output = model(images, training=False,
                   intermediates_dict=intermediates_dict)
output_shape = ((2, 2048, 1, 1) if data_format == 'channels_first' else
                (2, 1, 1, 2048))
self.assertEqual(output_shape, output.shape)

if data_format == 'channels_first':
    block_shapes = {
        'block0': (2, 64, 112, 112),
        'block0mp': (2, 64, 55, 55),
        'block1': (2, 256, 55, 55),
        'block2': (2, 512, 28, 28),
        'block3': (2, 1024, 7, 7),
        'block4': (2, 2048, 1, 1),
    }
else:
    block_shapes = {
        'block0': (2, 112, 112, 64),
        'block0mp': (2, 55, 55, 64),
        'block1': (2, 55, 55, 256),
        'block2': (2, 28, 28, 512),
        'block3': (2, 7, 7, 1024),
        'block4': (2, 1, 1, 2048),
    }
for (block_name, block) in intermediates_dict.items():
    self.assertEqual(block_shapes[block_name], block.shape)
