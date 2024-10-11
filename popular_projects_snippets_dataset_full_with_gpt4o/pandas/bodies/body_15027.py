# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
df = DataFrame(np.random.randn(100, 2))
df[2] = to_datetime(
    np.random.randint(
        812419200000000000,
        819331200000000000,
        size=100,
        dtype=np.int64,
    )
)

layout_to_expected_size = (
    {"layout": None, "expected_size": (2, 2)},  # default is 2x2
    {"layout": (2, 2), "expected_size": (2, 2)},
    {"layout": (4, 1), "expected_size": (4, 1)},
    {"layout": (1, 4), "expected_size": (1, 4)},
    {"layout": (3, 3), "expected_size": (3, 3)},
    {"layout": (-1, 4), "expected_size": (1, 4)},
    {"layout": (4, -1), "expected_size": (4, 1)},
    {"layout": (-1, 2), "expected_size": (2, 2)},
    {"layout": (2, -1), "expected_size": (2, 2)},
)

for layout_test in layout_to_expected_size:
    axes = df.hist(layout=layout_test["layout"])
    expected = layout_test["expected_size"]
    self._check_axes_shape(axes, axes_num=3, layout=expected)

# layout too small for all 4 plots
msg = "Layout of 1x1 must be larger than required size 3"
with pytest.raises(ValueError, match=msg):
    df.hist(layout=(1, 1))

# invalid format for layout
msg = re.escape("Layout must be a tuple of (rows, columns)")
with pytest.raises(ValueError, match=msg):
    df.hist(layout=(1,))
msg = "At least one dimension of layout must be positive"
with pytest.raises(ValueError, match=msg):
    df.hist(layout=(-1, -1))
