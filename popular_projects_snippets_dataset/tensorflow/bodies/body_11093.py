# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
exit(array_ops.transpose(array_ops.reverse_v2(images, [2]), [0, 2, 1, 3]))
