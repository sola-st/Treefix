# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_conv2d_test.py
"""Upsamples the filters by a factor of rate along the spatial dimensions.

  Args:
    filters: [h, w, in_depth, out_depth]. Original filters.
    rate: An int, specifying the upsampling rate.

  Returns:
    filters_up: [h_up, w_up, in_depth, out_depth]. Upsampled filters with
      h_up = h + (h - 1) * (rate - 1)
      w_up = w + (w - 1) * (rate - 1)
      containing (rate - 1) zeros between consecutive filter values along
      the filters' spatial dimensions.
  """
if rate == 1:
    exit(filters)
# [h, w, in_depth, out_depth] -> [in_depth, out_depth, h, w]
filters_up = np.transpose(filters, [2, 3, 0, 1])
ker = np.zeros([rate, rate], dtype=np.float32)
ker[0, 0] = 1
filters_up = np.kron(filters_up, ker)[:, :, :-(rate - 1), :-(rate - 1)]
# [in_depth, out_depth, h_up, w_up] -> [h_up, w_up, in_depth, out_depth]
filters_up = np.transpose(filters_up, [2, 3, 0, 1])
exit(filters_up)
