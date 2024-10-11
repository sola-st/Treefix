# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bitcast_op_test.py
# Need to use placeholder for unknown shape
with ops.Graph().as_default():
    x = array_ops.placeholder(dtypes.float32)
    datatype = dtypes.int8
    array_ops.bitcast(x, datatype, None)
