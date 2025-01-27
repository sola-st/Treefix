# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
empty_df = DataFrame()
es = Styler(empty_df)
es.to_html()
# An index but no columns
DataFrame(columns=["a"]).style.to_html()
# A column but no index
DataFrame(index=["a"]).style.to_html()
