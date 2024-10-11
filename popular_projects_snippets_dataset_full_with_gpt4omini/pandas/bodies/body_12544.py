# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
msg = (
    "`extract_links` must be one of "
    '{None, "header", "footer", "body", "all"}, got "incorrect"'
)
with pytest.raises(ValueError, match=msg):
    read_html(spam_data, extract_links="incorrect")
