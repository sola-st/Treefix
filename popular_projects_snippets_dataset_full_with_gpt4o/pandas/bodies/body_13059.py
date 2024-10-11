# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
frame = frame.copy()
frame.iloc[:5, frame.columns.get_loc("A")] = np.nan

frame.to_excel(path, "test1")
frame.to_excel(path, "test1", columns=["A", "B"])
frame.to_excel(path, "test1", header=False)
frame.to_excel(path, "test1", index=False)

# test roundtrip
frame.to_excel(path, "test1")
recons = pd.read_excel(path, sheet_name="test1", index_col=0)
tm.assert_frame_equal(frame, recons)

frame.to_excel(path, "test1", index=False)
recons = pd.read_excel(path, sheet_name="test1", index_col=None)
recons.index = frame.index
tm.assert_frame_equal(frame, recons)

frame.to_excel(path, "test1", na_rep="NA")
recons = pd.read_excel(path, sheet_name="test1", index_col=0, na_values=["NA"])
tm.assert_frame_equal(frame, recons)

# GH 3611
frame.to_excel(path, "test1", na_rep="88")
recons = pd.read_excel(path, sheet_name="test1", index_col=0, na_values=["88"])
tm.assert_frame_equal(frame, recons)

frame.to_excel(path, "test1", na_rep="88")
recons = pd.read_excel(
    path, sheet_name="test1", index_col=0, na_values=[88, 88.0]
)
tm.assert_frame_equal(frame, recons)

# GH 6573
frame.to_excel(path, "Sheet1")
recons = pd.read_excel(path, index_col=0)
tm.assert_frame_equal(frame, recons)

frame.to_excel(path, "0")
recons = pd.read_excel(path, index_col=0)
tm.assert_frame_equal(frame, recons)

# GH 8825 Pandas Series should provide to_excel method
s = frame["A"]
s.to_excel(path)
recons = pd.read_excel(path, index_col=0)
tm.assert_frame_equal(s.to_frame(), recons)
