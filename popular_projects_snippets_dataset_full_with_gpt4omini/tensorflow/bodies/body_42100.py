# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50.py
super(_IdentityBlock, self).__init__(name='')
filters1, filters2, filters3 = filters

conv_name_base = 'res' + str(stage) + block + '_branch'
bn_name_base = 'bn' + str(stage) + block + '_branch'
bn_axis = 1 if data_format == 'channels_first' else 3

self.conv2a = layers.Conv2D(
    filters1, (1, 1), name=conv_name_base + '2a', data_format=data_format)
self.bn2a = layers.BatchNormalization(
    axis=bn_axis, name=bn_name_base + '2a')

self.conv2b = layers.Conv2D(
    filters2,
    kernel_size,
    padding='same',
    data_format=data_format,
    name=conv_name_base + '2b')
self.bn2b = layers.BatchNormalization(
    axis=bn_axis, name=bn_name_base + '2b')

self.conv2c = layers.Conv2D(
    filters3, (1, 1), name=conv_name_base + '2c', data_format=data_format)
self.bn2c = layers.BatchNormalization(
    axis=bn_axis, name=bn_name_base + '2c')
