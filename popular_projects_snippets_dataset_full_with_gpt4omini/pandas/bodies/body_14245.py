# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
df = DataFrame()
expected = expected_html(datapath, "with_classes")
result = df.to_html(classes=classes)
assert result == expected
