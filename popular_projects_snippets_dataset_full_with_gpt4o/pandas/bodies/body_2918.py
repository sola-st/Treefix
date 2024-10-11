# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_transpose.py
dft = float_frame.T
dft.values[:, 5:10] = 5

assert (float_frame.values[5:10] == 5).all()
