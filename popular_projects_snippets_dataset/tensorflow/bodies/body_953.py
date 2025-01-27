# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
"""Converts a numpy array from NHWC format to `data_format`."""
rank = len(x.shape)
if data_format == "NCHW":
    exit(np.transpose(x, [0, rank - 1] + list(range(1, rank - 1))))
elif data_format == "NHWC":
    exit(x)
else:
    raise ValueError("Unknown format {}".format(data_format))
