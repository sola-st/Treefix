# Extracted from ./data/repos/pandas/pandas/tests/util/test_util.py
with pytest.raises(ValueError, match="Could not find file"):
    datapath("not_a_file")
