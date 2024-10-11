# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
inp1 = array_ops.placeholder(
    dtype=dtypes.float32, shape=[None, 1, 1], name="input1")
inp2 = array_ops.placeholder(
    dtype=dtypes.float32, shape=[None, 1, 1], name="input2")
var = variables.Variable([[[1.0]]], dtype=dtypes.float32, name="v1")
out = TrtConvertTest._GetGraph(inp1, inp2, var)
exit((g, var, inp1, inp2, out))
