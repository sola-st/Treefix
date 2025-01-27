# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-10982
write_frame = DataFrame({"A": [1, 1, 1], "B": [2, 2, 2]})

with pytest.raises(KeyError, match="Not all names specified"):
    write_frame.to_excel(path, "test1", columns=["B", "C"])

with pytest.raises(
    KeyError, match="'passes columns are not ALL present dataframe'"
):
    write_frame.to_excel(path, "test1", columns=["C", "D"])
