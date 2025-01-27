# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
styler = Styler(df, uuid="abc123")
result = styler.to_html()
assert "abc123" in result

styler = df.style
result = styler.set_uuid("aaa")
assert result is styler
assert result.uuid == "aaa"
