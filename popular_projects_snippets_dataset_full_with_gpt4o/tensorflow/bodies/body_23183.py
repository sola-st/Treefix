# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/testdata/gen_tf_variablev2_model.py
input1 = array_ops.placeholder(
    dtype=dtypes.float32, shape=[None, 1, 1], name="input1")
input2 = array_ops.placeholder(
    dtype=dtypes.float32, shape=[None, 1, 1], name="input2")
var1 = variable_scope.get_variable(
    "var1",
    shape=[1, 1, 1],
    initializer=init_ops.constant_initializer([[[13.]]]),
    dtype=dtypes.float32)
var2 = variable_scope.get_variable(
    "var2",
    shape=[1, 1, 1],
    initializer=init_ops.constant_initializer([[[37.]]]),
    dtype=dtypes.float32)
mul1 = input1 * var1
mul2 = input2 * var2
add = mul1 + mul2
sub = add - 45.
out = array_ops.identity(sub, name="output")
exit((g, input1, input2, out))
