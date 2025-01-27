# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/quantized_conv_ops_test.py
# Our generated input is [batch, rows, cols, depth], and looks like this:
# (1,2,3)    (4,5,6)    (7,8,9)
# (10,11,12) (13,14,15) (16,17,18)
# The filter data is [filter_height, filter_width, depth, filter_count]:
# ( 1, 4, 7) (10, 13, 16)
# (19,22,25) (28, 31, 34)
# -
# ( 2, 5, 8) (11, 14, 17)
# (20,23,26) (29, 32, 35)
# -
# ( 3, 6, 9) (12, 15, 18)
# (21,24,27) (30, 33, 36)
# The raw accumulated totals are:
# 1*1+2*4+3*7+4*10+5*13+6*16+10*19+11*22+12*25+13*28+14*31+15*34=2271
# 1*2+2*5+3*8+4*11+5*14+6*17+10*20+11*23+12*26+13*29+14*32+15*35=2367
# 1*3+2*6+3*9+4*12+5*15+6*18+10*21+11*24+12*27+13*30+14*33+15*36=2463
# 4*1+5*4+6*7+7*10+8*13+9*16+13*19+14*22+15*25+16*28+17*31+18*34=2901
# 4*2+5*5+6*8+7*11+8*14+9*17+13*20+14*23+15*26+16*29+17*32+18*35=3033
# 4*3+5*6+6*9+7*12+8*15+9*18+13*21+14*24+15*27+16*30+17*33+18*36=3165
# The expected values are taken from the raw totals and rescaled to fit into
# eight bits.
expected_output = [2271.0, 2367.0, 2463.0, 2901.0, 3033.0, 3165.0]
self._VerifyValues(
    tensor_in_sizes=[1, 2, 3, 3],
    filter_in_sizes=[2, 2, 3, 3],
    stride=1,
    padding="VALID",
    expected=expected_output)
