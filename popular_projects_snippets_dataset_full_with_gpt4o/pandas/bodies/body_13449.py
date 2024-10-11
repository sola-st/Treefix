# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py

string_array: StringArray | ArrowStringArray
string_array_na: StringArray | ArrowStringArray
if storage == "python":
    string_array = StringArray(np.array(["a", "b", "c"], dtype=np.object_))
    string_array_na = StringArray(np.array(["a", "b", pd.NA], dtype=np.object_))

else:
    pa = pytest.importorskip("pyarrow")
    string_array = ArrowStringArray(pa.array(["a", "b", "c"]))
    string_array_na = ArrowStringArray(pa.array(["a", "b", None]))

exit(DataFrame(
    {
        "a": Series([1, np.nan, 3], dtype="Int64"),
        "b": Series([1, 2, 3], dtype="Int64"),
        "c": Series([1.5, np.nan, 2.5], dtype="Float64"),
        "d": Series([1.5, 2.0, 2.5], dtype="Float64"),
        "e": Series([True, False, pd.NA], dtype="boolean"),
        "f": Series([True, False, True], dtype="boolean"),
        "g": string_array,
        "h": string_array_na,
    }
))
