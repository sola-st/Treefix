# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_matplotlib.py
# test giving a gmap in DataFrame but with wrong axis
msg = "'gmap' is a DataFrame but underlying data for operations is a Series"
with pytest.raises(ValueError, match=msg):
    styler_blank.background_gradient(gmap=gmap, axis=axis)._compute()
