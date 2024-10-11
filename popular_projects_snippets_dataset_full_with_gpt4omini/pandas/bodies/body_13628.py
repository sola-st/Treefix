# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
# gh 46037
result = styler.to_latex(environment="longtable", column_format="lrr{10cm}")
expected = r"\multicolumn{4}{r}{Continued on next page} \\"
assert expected in result
