# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
parser = all_parsers
data = DataFrame(
    {
        "Country": ["Venezuela", "Venezuela"],
        "Twitter": ["Hugo Chávez Frías", "Henrique Capriles R."],
    }
)
with tm.ensure_clean("test.tar.gz") as tar_path:
    data.to_csv(tar_path, index=False)

    # test that read_csv infers .tar.gz to gzip:
    tm.assert_frame_equal(parser.read_csv(tar_path), data)

    # test that file is indeed gzipped:
    with tarfile.open(tar_path, "r:gz") as tar:
        result = parser.read_csv(
            tar.extractfile(tar.getnames()[0]), compression="infer"
        )
        tm.assert_frame_equal(result, data)
