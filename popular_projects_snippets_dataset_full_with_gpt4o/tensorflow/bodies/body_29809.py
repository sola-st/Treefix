# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
block_size_sq = block_size * block_size
if data_format == "NHWC":
    b, ih, iw, ic = tensor.shape.as_list()
    assert ic % block_size_sq == 0, (ic, block_size_sq)
    ow, oh, oc = iw * block_size, ih * block_size, ic // block_size_sq
    tensor = array_ops.reshape(tensor,
                               [b, ih, iw, block_size, block_size, oc])
    tensor = array_ops.transpose(tensor, [0, 1, 3, 2, 4, 5])
    tensor = array_ops.reshape(tensor, [b, oh, ow, oc])
elif data_format == "NCHW":
    b, ic, ih, iw = tensor.shape.as_list()
    assert ic % block_size_sq == 0, (ic, block_size_sq)
    ow, oh, oc = iw * block_size, ih * block_size, ic // block_size_sq
    tensor = array_ops.reshape(tensor,
                               [b, block_size, block_size, oc, ih, iw])
    tensor = array_ops.transpose(tensor, [0, 3, 4, 1, 5, 2])
    tensor = array_ops.reshape(tensor, [b, oc, oh, ow])
exit(tensor)
