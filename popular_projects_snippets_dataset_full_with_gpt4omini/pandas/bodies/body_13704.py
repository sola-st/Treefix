# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_matplotlib.py
# GH 12145
df = DataFrame(range(5))
ctx = df.style.background_gradient(vmin=1, vmax=3)._compute().ctx
assert ctx[(0, 0)] == ctx[(1, 0)]
assert ctx[(4, 0)] == ctx[(3, 0)]
