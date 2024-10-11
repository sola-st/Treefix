# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
parser = all_parsers
compress_kwargs = {"compression": invalid_compression}

msg = f"Unrecognized compression type: {invalid_compression}"

with pytest.raises(ValueError, match=msg):
    parser.read_csv("test_file.zip", **compress_kwargs)
