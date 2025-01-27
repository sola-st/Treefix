# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#43344
ser = pd.Series(["AA", "BB", "CC", "DD", "EE", "", pd.NA], dtype="string")
regex_mapping = {
    "AA": "CC",
    "BB": "CC",
    "EE": "CC",
    "CC": "CC-REPL",
}
result = ser.replace(regex_mapping, regex=True)
exp = pd.Series(["CC", "CC", "CC-REPL", "DD", "CC", "", pd.NA], dtype="string")
tm.assert_series_equal(result, exp)
