# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
df = DataFrame(
    {"A": [6, 30000, 2], "B": [1, 2, 70000], "C": [223442, 0, 1]},
    columns=["A", "B", "C"],
)
result = df.to_html(justify=justify)
expected = expected_html(datapath, "justify").format(justify=justify)
assert result == expected
