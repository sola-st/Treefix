# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
parser, data, expected = parser_and_data

with tm.ensure_clean("combined_zip.zip") as path:
    inner_file_names = ["test_file", "second_file"]

    with zipfile.ZipFile(path, mode="w") as tmp:
        for file_name in inner_file_names:
            tmp.writestr(file_name, data)

    with pytest.raises(ValueError, match="Multiple files"):
        parser.read_csv(path, compression=compression)
