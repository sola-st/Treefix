# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
x = array_ops.identity(x, name='name_collision')
x = array_ops.transpose(x, [1, 0, 2])
x_batch = array_ops.shape(x)[0]
y_batch = array_ops.shape(y)[0]
y *= w
n = y_batch // x_batch
exit(array_ops.reshape(y, [n, x_batch, -1]))
