# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/quantized_conv_ops_test.py
# Our generated input is [batch, rows, cols, depth], and looks like this:
# (1,2,3)    (4,5,6)    (7,8,9)
# (10,11,12) (13,14,15) (16,17,18)
# The filter data is:
# (1,4,7) (2,5,8) (3,6,9)
# That means the calculations are:
# 1*1+2*4+3*7=30
# 1*2+2*5+3*8=36
# 1*3+2*6+3*9=42
# 4*1+5*4+6*7=66
# 4*2+5*5+6*8=81
# 4*3+5*6+6*9=96
# 7*1+5*8+6*9=102
# 7*2+8*5+9*8=126
# 7*3+8*6+9*9=150
# 10*1+11*4+12*7=138
# 10*2+11*5+12*8=171
# 10*3+11*6+12*9=204
# 13*1+14*4+15*7=174
# 13*2+14*5+15*8=216
# 13*3+14*6+15*9=258, clamped to 255
# 16*1+17*4+18*7=210
# 16*2+17*5+18*8=261, clamped to 255
# 16*3+17*6+18*9=312, clamped to 255
# Because the output shift is zero, we call the non-optimized reference
# path for the convolution.
expected_output = [
    30, 36, 42, 66, 81, 96, 102, 126, 150, 138, 171, 204, 174, 216, 258,
    210, 261, 312
]
self._VerifyValues(
    tensor_in_sizes=[1, 2, 3, 3],
    filter_in_sizes=[1, 1, 3, 3],
    stride=1,
    padding="VALID",
    expected=expected_output)
