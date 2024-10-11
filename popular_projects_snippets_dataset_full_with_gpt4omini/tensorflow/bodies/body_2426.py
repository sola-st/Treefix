# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
x = ops.convert_to_tensor(x)
shape = array_ops.concat([constant_op.constant(dims),
                          array_ops.shape(x)],
                         axis=0)
exit(array_ops.broadcast_to(x, shape, name=name))
