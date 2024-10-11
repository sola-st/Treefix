# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
"""Compute depthwise_conv2d using Numpy.

  This allows use to test TensorFlow's depthwise_conv2d by comparing to the
  Numpy version.

  Args:
    x1: The input Numpy array, in NHWC format.
    x2: The filter Numpy array.
    strides: A Python list of 4 elements representing the strides.

  Returns:
    The depthwise conv2d output as a Numpy array.
  """
n, h, w, c = x1.shape
fh, fw, c2, o = x2.shape
assert c == c2
_, sh, sw, _ = strides
out_rows = (h - fh + sh) // sh
out_cols = (w - fw + sw) // sw
out = np.zeros([n, out_rows, out_cols, c * o])
for i in range(out_rows):
    for j in range(out_cols):
        for k in range(c):
            start_height = i * sh
            end_height = start_height + fh
            start_width = j * sw
            end_width = start_width + fw
            # multiplied_slice.shape: (b, fh, fw, o)
            multiplied_slice = (
                x1[:, start_height:end_height, start_width:end_width, k, np.newaxis]
                * x2[:, :, k, :])
            # Set a slice of b * o elements of 'out'.
            out[:, i, j, k * o:(k + 1) * o] = np.sum(multiplied_slice, axis=(1, 2))
exit(out)
