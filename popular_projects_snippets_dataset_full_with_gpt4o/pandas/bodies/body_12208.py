# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
parser, data, expected = parser_and_data

with tm.ensure_clean("test_file.zip") as path:
    with zipfile.ZipFile(path, mode="w") as tmp:
        tmp.writestr("test_file", data)

    if compression == "zip2":
        with open(path, "rb") as f:
            result = parser.read_csv(f, compression="zip")
    else:
        result = parser.read_csv(path, compression=compression)

    tm.assert_frame_equal(result, expected)
