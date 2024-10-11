# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# see gh-32207
basename = "test_spaces"

actual = pd.read_excel(basename + read_ext)
expected = DataFrame(
    {
        "testcol": [
            "this is great",
            "4    spaces",
            "1 trailing ",
            " 1 leading",
            "2  spaces  multiple  times",
        ]
    }
)
tm.assert_frame_equal(actual, expected)
