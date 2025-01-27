# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
df = self._bank_data(banklist_data, index_col=[0, 1])[0]
assert isinstance(df.index, MultiIndex)
