# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
parser, _, _ = parser_and_data

with tm.ensure_clean() as path:
    with open(path, "rb") as f:
        with pytest.raises(zipfile.BadZipfile, match="File is not a zip file"):
            parser.read_csv(f, compression="zip")
