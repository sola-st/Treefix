# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/identity_output_test.py
x1 = math_ops.exp(x)
x1 = x1 + x

out1 = array_ops.identity(x1, name='output_0')
out2 = array_ops.identity(x1, name='output_1')
iden1 = array_ops.identity(x1)
out3 = array_ops.identity(iden1, name='output_2')
exit([out1, out2, out3])
