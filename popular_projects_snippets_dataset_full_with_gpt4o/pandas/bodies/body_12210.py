# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
parser, _, _ = parser_and_data

with tm.ensure_clean() as path:
    with zipfile.ZipFile(path, mode="w"):
        pass

    with pytest.raises(ValueError, match="Zero files"):
        parser.read_csv(path, compression="zip")
