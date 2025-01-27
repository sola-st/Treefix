# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
msg = r"'chunksize' must be an integer >=1"

with pytest.raises(ValueError, match=msg):
    with read_json(StringIO(lines_json_df), lines=True, chunksize=chunksize) as _:
        pass
