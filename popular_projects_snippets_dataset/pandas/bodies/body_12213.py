# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
# see gh-9770
parser = all_parsers
kwargs = {"index_col": 0, "parse_dates": True}

expected = parser.read_csv(csv1, **kwargs)
kwargs["compression"] = "infer"

if buffer:
    with open(csv1) as f:
        result = parser.read_csv(f, **kwargs)
else:
    ext = "." + ext if ext else ""
    result = parser.read_csv(csv1 + ext, **kwargs)

tm.assert_frame_equal(result, expected)
