# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_iterator.py
parser = all_parsers
kwargs = {"header": None}

with tm.ensure_clean() as path:
    with open(path, "w") as f:
        f.write("AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG")

    with open(path) as f:
        for line in f:
            if "CCC" in line:
                break

        result = parser.read_csv(f, **kwargs)
        expected = DataFrame({0: ["DDD", "EEE", "FFF", "GGG"]})
        tm.assert_frame_equal(result, expected)
