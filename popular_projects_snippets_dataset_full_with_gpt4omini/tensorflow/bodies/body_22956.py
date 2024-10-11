# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
"""Normalizes the pixel values to lay within the [-1, 1] range.

   The same normalization shall be used during training and inference.
  """
x, y = entry['image'], entry['label']
x = math_ops.cast(x, dtypes.float32)
x = 2.0 * (x / 255.0) - 1.0
y = math_ops.cast(y, dtypes.int32)
exit((x, y))
