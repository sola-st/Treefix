# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
values = float_frame.values.astype(int)
frame = DataFrame(values, index=float_frame.index, columns=float_frame.columns)
deltas = frame * timedelta(1)
deltas.sum()
