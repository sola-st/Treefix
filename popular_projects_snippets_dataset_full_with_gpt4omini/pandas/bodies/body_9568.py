# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
# GH#44715
with pytest.raises(TypeError, match="data type 'Float16' not understood"):
    pd.array([1.0, 2.0], dtype="Float16")
