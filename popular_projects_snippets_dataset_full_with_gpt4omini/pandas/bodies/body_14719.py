# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_hist_box_by.py
# GH 15079, test if error is raised when invalid layout is given

with pytest.raises(ValueError, match=msg):
    hist_df.plot.box(column=["A", "B"], by=by, layout=layout)
