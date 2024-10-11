# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/testdata/gen_tftrt_model.py
"""Define graph."""
add = input1 + var
mul = input1 * add
add = mul + add
add = add + input2
out = array_ops.identity(add, name="output")
exit(out)
