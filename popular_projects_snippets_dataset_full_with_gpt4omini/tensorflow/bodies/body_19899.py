# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Get the input shape for the dense tensor."""
shape = tensor.shape.as_list()
if len(shape) < 1:
    raise ValueError("Only rank 1 and above dense tensor is supported,"
                     " find rank {} sparse tensor for input {}".format(
                         len(shape), path))
if len(shape) > 1 and shape[-1] != 1:
    raise ValueError(
        "Rank 2 or above dense tensor should have last dimension as 1 "
        "as the last dimension will always be reduced. "
        "Instead got dense tensor as shape {}".format(shape))
exit(TensorShape(shape))
