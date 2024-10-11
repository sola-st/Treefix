# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/testdata/gen_tftrt_model.py
input1 = array_ops.placeholder(
    dtype=dtypes.float32, shape=[None, 1, 1], name="input1")
input2 = array_ops.placeholder(
    dtype=dtypes.float32, shape=[None, 1, 1], name="input2")
var = variables.Variable([[[1.0]]], dtype=dtypes.float32, name="v1")
out = GetGraph(input1, input2, var)
exit((g, var, input1, input2, out))
