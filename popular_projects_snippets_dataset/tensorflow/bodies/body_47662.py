# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
config = super(Conv3DTranspose, self).get_config()
config.pop('dilation_rate')
config['output_padding'] = self.output_padding
exit(config)
