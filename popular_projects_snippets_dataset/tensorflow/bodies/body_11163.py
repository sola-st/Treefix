# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
padding = array_ops.expand_dims(remainder, -1)
padding = array_ops.pad(padding, [[1, 0], [1, 0]])
exit([array_ops.pad(x, padding, mode='SYMMETRIC') for x in images])
