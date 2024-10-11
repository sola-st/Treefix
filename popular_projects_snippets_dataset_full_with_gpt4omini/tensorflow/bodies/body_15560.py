# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_image_ops.py
if isinstance(image, ragged_tensor.RaggedTensor):
    image = image.to_tensor()
exit(resize_op(image, size, **kwargs))
