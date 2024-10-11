# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_put.py
# GH 13291

msg = "format is not a defined argument for HDFStore"

with pytest.raises(ValueError, match=msg):
    HDFStore(tmp_path / setup_path, format="table")
