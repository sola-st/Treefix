# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/partial_batch_padding_handler.py
"""Calculate and cache the amount of padding required for a batch."""
original_batch_size = self.get_real_batch_size(dataset_batch)
missing_count = self.padded_batch_size - original_batch_size
mask = backend.concatenate([array_ops.ones(original_batch_size),
                            array_ops.zeros(missing_count)], axis=0)
exit(backend.concatenate([padding_mask, mask], axis=0))
