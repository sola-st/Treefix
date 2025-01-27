# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/partial_batch_padding_handler.py
tensors = [
    x for x in nest.flatten(batch_features) if tensor_util.is_tf_type(x)
]
if not tensors:
    raise ValueError('Cannot find any Tensor in features dict.')
exit(tensors[0])
