# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
block_size_sq = block_size * block_size

dtype = tensor.dtype
if dtype == dtypes.qint8:
    tensor = array_ops.bitcast(tensor, dtypes.int8)

if data_format == "NHWC":
    b, ih, iw, ic = tensor.shape.as_list()
    assert ih % block_size == 0, (ih, block_size)
    assert iw % block_size == 0, (iw, block_size)
    ow, oh, oc = iw // block_size, ih // block_size, ic * block_size_sq
    tensor = array_ops.reshape(tensor,
                               [b, oh, block_size, ow, block_size, ic])
    tensor = array_ops.transpose(tensor, [0, 1, 3, 2, 4, 5])
    tensor = array_ops.reshape(tensor, [b, oh, ow, oc])
elif data_format == "NCHW":
    b, ic, ih, iw = tensor.shape.as_list()
    assert ih % block_size == 0, (ih, block_size)
    assert iw % block_size == 0, (iw, block_size)
    ow, oh, oc = iw // block_size, ih // block_size, ic * block_size_sq
    tensor = array_ops.reshape(tensor,
                               [b, ic, oh, block_size, ow, block_size])
    tensor = array_ops.transpose(tensor, [0, 3, 5, 1, 2, 4])
    tensor = array_ops.reshape(tensor, [b, oc, oh, ow])

if dtype == dtypes.qint8:
    tensor = array_ops.bitcast(tensor, dtype)
exit(tensor)
