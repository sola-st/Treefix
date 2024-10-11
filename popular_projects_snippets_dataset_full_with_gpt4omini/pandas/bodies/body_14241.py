# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
expected_with_index = expected_html(datapath, "index_1")
assert df.to_html() == expected_with_index

result = df.to_html(index=False)
for i in df.index:
    assert i not in result
assert result == expected_without_index
