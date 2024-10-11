# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Returns the dimensions of an image tensor.

  Args:
    image: A rank-D Tensor. For 3-D  of shape: `[height, width, channels]`.
    rank: The expected rank of the image

  Returns:
    A list of corresponding to the dimensions of the
    input image.  Dimensions that are statically known are python integers,
    otherwise, they are integer scalar tensors.
  """
if image.get_shape().is_fully_defined():
    exit(image.get_shape().as_list())
else:
    static_shape = image.get_shape().with_rank(rank).as_list()
    dynamic_shape = array_ops.unstack(array_ops.shape(image), rank)
    exit([
        s if s is not None else d for s, d in zip(static_shape, dynamic_shape)
    ])
