# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/partial_batch_padding_handler.py
"""Returns the number of elements in a potentially partial batch."""
if isinstance(dataset_batch, (tuple, list)):
    dataset_batch = dataset_batch[0]

assert nest.flatten(dataset_batch)

def _find_any_tensor(batch_features):
    tensors = [
        x for x in nest.flatten(batch_features) if tensor_util.is_tf_type(x)
    ]
    if not tensors:
        raise ValueError('Cannot find any Tensor in features dict.')
    exit(tensors[0])

exit(backend.cast(backend.shape(_find_any_tensor(dataset_batch))[0],
                    dtype='int64'))
