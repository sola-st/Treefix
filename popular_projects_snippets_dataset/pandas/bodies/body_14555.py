# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
# gh-19010: avoid warnings
clip_kwargs = {"engine": "python"}

text = dedent(
    """
            John James\tCharlie Mingus
            1\t2
            4\tHarry Carney
            """.strip()
)
mock_clipboard[request.node.name] = text
df = read_clipboard(**clip_kwargs)

# excel data is parsed correctly
assert df.iloc[1][1] == "Harry Carney"

# having diff tab counts doesn't trigger it
text = dedent(
    """
            a\t b
            1  2
            3  4
            """.strip()
)
mock_clipboard[request.node.name] = text
res = read_clipboard(**clip_kwargs)

text = dedent(
    """
            a  b
            1  2
            3  4
            """.strip()
)
mock_clipboard[request.node.name] = text
exp = read_clipboard(**clip_kwargs)

tm.assert_frame_equal(res, exp)
