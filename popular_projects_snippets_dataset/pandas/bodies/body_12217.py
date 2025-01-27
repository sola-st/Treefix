# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
parser = all_parsers
df = DataFrame({"a": [0, 1]})
with tm.ensure_clean("test.csv") as path_csv:
    with tm.ensure_clean("test.csv.zip") as path_zip:
        # make sure to create un-compressed file with zip extension
        df.to_csv(path_csv, index=False)
        Path(path_zip).write_text(Path(path_csv).read_text())

        tm.assert_frame_equal(parser.read_csv(path_zip, compression=None), df)
