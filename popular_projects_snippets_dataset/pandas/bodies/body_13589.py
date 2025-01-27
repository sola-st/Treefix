# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
styler.set_table_styles(
    [
        {"selector": "mycommand", "props": ":{myoptions}"},
        {"selector": "mycommand2", "props": ":{myoptions2}"},
    ]
)
expected = dedent(
    """\
        \\begin{table}
        \\mycommand{myoptions}
        \\mycommand2{myoptions2}
        """
)
assert expected in styler.to_latex()
