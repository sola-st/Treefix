# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
config = super(DepthwiseConv2D, self).get_config()
config.pop('filters')
config.pop('kernel_initializer')
config.pop('kernel_regularizer')
config.pop('kernel_constraint')
config['depth_multiplier'] = self.depth_multiplier
config['depthwise_initializer'] = initializers.serialize(
    self.depthwise_initializer)
config['depthwise_regularizer'] = regularizers.serialize(
    self.depthwise_regularizer)
config['depthwise_constraint'] = constraints.serialize(
    self.depthwise_constraint)
exit(config)
