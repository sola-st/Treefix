# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer_test.py
var0 = resource_variable_ops.ResourceVariable(
    [1.0, 2.0], dtype=dtype, trainable=False, name='a')
var1 = resource_variable_ops.ResourceVariable(
    [3.0, 4.0], dtype=dtype, trainable=False, name='b')
exit(5 * var0 + var1)
