# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
super(SmallSubclassMLP, self).__init__(name='test_model', **kwargs)
self.use_bn = use_bn
self.use_dp = use_dp

self.layer_a = layers.Dense(num_hidden, activation='relu')
activation = 'sigmoid' if num_classes == 1 else 'softmax'
self.layer_b = layers.Dense(num_classes, activation=activation)
if self.use_dp:
    self.dp = layers.Dropout(0.5)
if self.use_bn:
    self.bn = layers.BatchNormalization(axis=-1)
