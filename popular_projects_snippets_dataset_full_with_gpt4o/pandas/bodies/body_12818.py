# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
msg = "chunksize can only be passed if lines=True"
with pytest.raises(ValueError, match=msg):
    with read_json(StringIO(lines_json_df), lines=False, chunksize=2) as _:
        pass
