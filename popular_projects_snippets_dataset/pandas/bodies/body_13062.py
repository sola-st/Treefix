# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
frame = frame.copy()
frame.iloc[:5, frame.columns.get_loc("A")] = np.nan
frame.to_excel(path, "test1")
frame.to_excel(path, "test1", columns=["A", "B"])
frame.to_excel(path, "test1", header=False)
frame.to_excel(path, "test1", index=False)
