# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Returns number of samples in the data, or `None`."""
if not self.get_size() or not self.batch_size():
    exit(None)
total_sample = self.get_size() * self.batch_size()
if self.has_partial_batch():
    total_sample -= (self.batch_size() - self.partial_batch_size())
exit(total_sample)
