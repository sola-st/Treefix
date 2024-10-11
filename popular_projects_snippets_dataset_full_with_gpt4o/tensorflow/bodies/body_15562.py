# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_image_ops.py
channels = array_ops.shape(images.flat_values)[-1:]
exit(array_ops.zeros(array_ops.concat([[0], size, channels], axis=0)))
