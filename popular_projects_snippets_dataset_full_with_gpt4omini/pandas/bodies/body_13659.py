# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
# GH 43619
result = (
    styler_mi.set_uuid("")
    .applymap(lambda v: "color: blue;")
    .hide(styler_mi.data.columns[1:], axis="columns")
    .hide(styler_mi.data.index[1:], axis="index")
    .to_html()
)
expected_styles = dedent(
    """\
        <style type="text/css">
        #T__row0_col0 {
          color: blue;
        }
        </style>
        """
)
assert expected_styles in result
