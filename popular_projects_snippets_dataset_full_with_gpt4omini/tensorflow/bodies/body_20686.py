# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
x = ta_x.read(i)
next_c, next_h = _lstm_cell(c, h, x)
exit((i + 1, next_c, next_h, ta_x))
