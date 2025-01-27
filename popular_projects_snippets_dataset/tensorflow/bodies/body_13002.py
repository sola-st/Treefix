# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
x_shape = array_ops.shape(x)
packed_shape = array_ops.stack(shape)
exit(control_flow_ops.Assert(
    math_ops.reduce_all(math_ops.equal(x_shape, packed_shape)), [
        "Expected shape for Tensor %s is " % x.name, packed_shape,
        " but saw shape: ", x_shape
    ]))
