# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Get the graph for testing."""
# The graph computes: inp1^2 + inp1*var + inp1 + inp2 + var
add = inp1 + var
mul = inp1 * add
add = mul + add
add = add + inp2
out = array_ops.identity(add, name="output")
exit(out)
