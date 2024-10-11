# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 30346
df = DataFrame({k: np.random.random(100) for k in "ABC"})
kwd = {props: {"color": "C1"}}
result = df.plot.box(return_type="dict", **kwd)

assert result[expected][0].get_color() == "C1"
