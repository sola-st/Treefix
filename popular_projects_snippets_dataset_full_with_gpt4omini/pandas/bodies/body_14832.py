# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
ax_df = DataFrame([0]).plot(
    secondary_y=secondary_y, ylabel="Y", ylim=(0, 100), yticks=[99]
)
for ax in ax_df.figure.axes:
    if ax.yaxis.get_visible():
        assert ax.get_ylabel() == "Y"
        assert ax.get_ylim() == (0, 100)
        assert ax.get_yticks()[0] == 99
