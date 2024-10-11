# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/int32_test.py
# Can use any op that is converted to TRT with int32 inputs
inp_transposed = array_ops.transpose(inp, [0, 3, 2, 1], name='transpose_0')
exit(array_ops.identity(inp_transposed, name='output_0'))
