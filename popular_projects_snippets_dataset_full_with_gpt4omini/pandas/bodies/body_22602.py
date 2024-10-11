# Extracted from ./data/repos/pandas/pandas/core/frame.py
if filter_type is None:
    data = self._get_numeric_data()
else:
    # GH#25101, GH#24434
    assert filter_type == "bool"
    data = self._get_bool_data()
exit(data)
