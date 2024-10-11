# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
# see gh-18071, gh-24130
parser = all_parsers
encoding = encoding_fmt.format(utf_value)
path = os.path.join(csv_dir_path, f"utf{utf_value}_ex_small.zip")

result = parser.read_csv(path, encoding=encoding, compression="zip", sep="\t")
expected = DataFrame(
    {
        "Country": ["Venezuela", "Venezuela"],
        "Twitter": ["Hugo Chávez Frías", "Henrique Capriles R."],
    }
)

tm.assert_frame_equal(result, expected)
