# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
# GH 33389
import matplotlib.pyplot as plt

df = DataFrame({"x": [1, 2, 3], "y": [1, 3, 2], "c": [1, 2, 3]})
df["x2"] = df["x"] + 1

fig, ax = plt.subplots()
df.plot("x", "y", c="c", kind="scatter", cmap="cividis", ax=ax)
df.plot("x2", "y", c="c", kind="scatter", cmap="magma", ax=ax)

assert ax.collections[0].cmap.name == "cividis"
assert ax.collections[1].cmap.name == "magma"
