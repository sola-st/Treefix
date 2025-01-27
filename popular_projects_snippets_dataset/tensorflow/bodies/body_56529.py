# Extracted from ./data/repos/tensorflow/tensorflow/lite/tutorials/dataset.py
"""Validate that filename corresponds to labels for the MNIST dataset."""
with tf.gfile.Open(filename, 'rb') as f:
    magic = read32(f)
    read32(f)  # num_items, unused
    if magic != 2049:
        raise ValueError('Invalid magic number %d in MNIST file %s' % (magic,
                                                                       f.name))
