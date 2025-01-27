# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
result = styler.to_latex(
    label=label[0],
    position=position[0],
    caption=caption[0],
    column_format=column_format[0],
    position_float=position_float[0],
)
assert label[1] in result
assert position[1] in result
assert caption[1] in result
assert column_format[1] in result
assert position_float[1] in result
