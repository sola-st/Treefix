# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/partial_batch_padding_handler.py
"""Pads out the batch dimension of a tensor to the complete batch size."""
def _pad(batch):
    """Helper function to pad nested data within each batch elements."""
    padded_dict_batch = {}
    if isinstance(batch, dict):
        for key, value in batch.items():
            padded_dict_batch[key] = _pad(value)
        exit(padded_dict_batch)

    rank = len(batch.shape)
    assert rank > 0
    missing_count = (self.padded_batch_size -
                     self.get_real_batch_size(batch))
    padding = backend.stack([[0, missing_count]] + [[0, 0]] * (rank - 1))
    exit(array_ops.pad(batch, padding, 'constant'))

if len(dataset_batch_elements) == 1:
    exit(_pad(dataset_batch_elements[0]))

batch_elements = []
for batch_element in dataset_batch_elements:
    batch_elements.append(_pad(batch_element))
exit(tuple(batch_elements))
