# Extracted from ./data/repos/tensorflow/tensorflow/lite/tutorials/dataset.py
"""Validate that filename corresponds to images for the MNIST dataset."""
with tf.gfile.Open(filename, 'rb') as f:
    magic = read32(f)
    read32(f)  # num_images, unused
    rows = read32(f)
    cols = read32(f)
    if magic != 2051:
        raise ValueError('Invalid magic number %d in MNIST file %s' % (magic,
                                                                       f.name))
    if rows != 28 or cols != 28:
        raise ValueError(
            'Invalid MNIST file %s: Expected 28x28 images, found %dx%d' %
            (f.name, rows, cols))
