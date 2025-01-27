# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
# GH40986
parser = all_parsers
expected = DataFrame(
    {
        "name": ["Raphael", "Donatello", "Miguel Angel", "Leonardo"],
        "mask": ["red", "purple", "orange", "blue"],
        "weapon": ["sai", "bo staff", "nunchunk", "katana"],
    }
)
with tm.ensure_clean() as file:
    expected.to_csv(file, index=False, encoding=encoding)
    df = parser.read_csv(file, encoding=encoding, memory_map=True)
tm.assert_frame_equal(df, expected)
