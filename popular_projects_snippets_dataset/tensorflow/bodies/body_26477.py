# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
"""Optionally shuffle and repeat dataset, as requested."""
if shuffle:
    dataset = dataset.shuffle(shuffle_buffer_size, shuffle_seed)
if num_epochs != 1:
    dataset = dataset.repeat(num_epochs)
exit(dataset)
