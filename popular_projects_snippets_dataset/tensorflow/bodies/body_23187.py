# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/testdata/gen_tf_readvariableop_model.py
mul1 = input1 * self.var1
mul2 = input2 * self.var2
add = mul1 + mul2
sub = add - 45.
exit(array_ops.identity(sub, name="output"))
