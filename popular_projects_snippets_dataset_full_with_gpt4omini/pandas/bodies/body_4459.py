# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame(float_frame["A"], index=float_frame.index, columns=["A"])
df.copy()
