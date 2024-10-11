# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
df = DataFrame({"x": [1, 2], "y": [3, 4]})
# passing both 'color' and 'style' arguments should be allowed
# if there is no color symbol in the style strings:
ax = df.plot(color=["red", "black"], style=["-", "--"])
# check that the linestyles are correctly set:
linestyle = [line.get_linestyle() for line in ax.lines]
assert linestyle == ["-", "--"]
# check that the colors are correctly set:
color = [line.get_color() for line in ax.lines]
assert color == ["red", "black"]
# passing both 'color' and 'style' arguments should not be allowed
# if there is a color symbol in the style strings:
msg = (
    "Cannot pass 'style' string with a color symbol and 'color' keyword "
    "argument. Please use one or the other or pass 'style' without a color "
    "symbol"
)
with pytest.raises(ValueError, match=msg):
    df.plot(color=["red", "black"], style=["k-", "r--"])
