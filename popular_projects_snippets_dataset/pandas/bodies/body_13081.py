# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# Test writing and re-reading a MI without the index. GH 5616.

# Initial non-MI frame.
frame1 = DataFrame({"a": [10, 20], "b": [30, 40], "c": [50, 60]})

# Add a MI.
frame2 = frame1.copy()
multi_index = MultiIndex.from_tuples([(70, 80), (90, 100)])
frame2.index = multi_index

# Write out to Excel without the index.
frame2.to_excel(path, "test1", index=False)

# Read it back in.
with ExcelFile(path) as reader:
    frame3 = pd.read_excel(reader, sheet_name="test1")

# Test that it is the same as the initial frame.
tm.assert_frame_equal(frame1, frame3)
