# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
"""Gets a concrete tensor shape without dynamic dimensions."""
if tensor_shape.unknown_rank:
    raise ValueError("Cannot generates random tensors for unknown rank!")
shape = [dim.size for dim in tensor_shape.dim]
if not shape:
    raise ValueError("The tensor cannot have a rank of 0!")
if shape[0] < 0:
    if batch_size is None or batch_size <= 0:
        raise ValueError("Must provide a valid batch size "
                         "as the tensor has a dynamic batch size!")
    shape[0] = batch_size
if any(filter(lambda x: x < 0, shape)):
    raise ValueError("Cannot have dynamic dimensions except for batch size!")
exit(shape)
