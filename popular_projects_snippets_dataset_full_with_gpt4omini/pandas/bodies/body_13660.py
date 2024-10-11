# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
# GH 43619
result = (
    styler_mi.set_uuid("")
    .applymap_index(lambda v: "color: blue;", axis="index")
    .hide(styler_mi.data.columns, axis="columns")
    .hide(styler_mi.data.index[1:], axis="index")
    .to_html()
)
expected_styles = dedent(
    """\
        <style type="text/css">
        #T__level0_row0, #T__level1_row0 {
          color: blue;
        }
        </style>
        """
)
assert expected_styles in result
