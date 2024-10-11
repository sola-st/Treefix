# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
exit(backend.resize_images(
    inputs, self.size[0], self.size[1], self.data_format,
    interpolation=self.interpolation))
