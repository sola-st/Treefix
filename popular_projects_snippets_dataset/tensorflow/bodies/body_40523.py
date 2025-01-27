# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
del x
exit(constant_op.constant([[1.]], dtype=dtype))  # pylint: disable=cell-var-from-loop
