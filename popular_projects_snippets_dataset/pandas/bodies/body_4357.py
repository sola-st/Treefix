# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame([datetime.now(), datetime.now()])
assert df[0].dtype == np.dtype("M8[ns]")
