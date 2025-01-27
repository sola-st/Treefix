# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
config = super(Conv2DTranspose, self).get_config()
config['output_padding'] = self.output_padding
exit(config)
