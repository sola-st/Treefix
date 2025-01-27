# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_compression.py
with tm.ensure_clean() as path:
    msg = "Unrecognized compression type: unsupported"
    with pytest.raises(ValueError, match=msg):
        pd.read_json(path, compression="unsupported")
