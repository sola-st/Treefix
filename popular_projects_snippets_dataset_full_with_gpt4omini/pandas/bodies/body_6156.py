# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# GH#38733
data = data_missing_for_sorting

with pytest.raises(NotImplementedError, match=""):
    data.argmin(skipna=False)

with pytest.raises(NotImplementedError, match=""):
    data.argmax(skipna=False)
