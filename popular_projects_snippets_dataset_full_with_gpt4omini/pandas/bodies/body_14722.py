# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_legend.py
# https://github.com/pandas-dev/pandas/issues/40044
df = DataFrame({"a": [1, 1], "b": [2, 3]})
df2 = DataFrame({"d": [2.5, 2.5]})

ax = df.plot(legend=True, color={"a": "blue", "b": "green"}, secondary_y="b")
df2.plot(legend=True, color={"d": "red"}, ax=ax)
legend = ax.get_legend()
result = [handle.get_color() for handle in legend.legendHandles]
expected = ["blue", "green", "red"]
assert result == expected
