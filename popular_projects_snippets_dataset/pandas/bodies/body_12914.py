# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_compression.py
df = pd.read_json('{"a": [1, 2, 3], "b": [4, 5, 6]}')
with tm.ensure_clean() as path:
    msg = "Unrecognized compression type: unsupported"
    with pytest.raises(ValueError, match=msg):
        df.to_json(path, compression="unsupported")
