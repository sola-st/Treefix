# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
index = lexsorted_two_level_string_multiindex
ser = Series(np.random.randn(len(index)), index=index, name="sth")

result = indexer_sl(ser)["foo"]
assert result.name == ser.name
