# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_excel.py
# see gh-18392
css = (
    f"border-top-color: {input_color}; "
    f"border-right-color: {input_color}; "
    f"border-bottom-color: {input_color}; "
    f"border-left-color: {input_color}; "
    f"background-color: {input_color}; "
    f"color: {input_color}"
)

expected = {}

expected["fill"] = {"patternType": "solid", "fgColor": output_color}

expected["font"] = {"color": output_color}

expected["border"] = {
    k: {"color": output_color, "style": "none"}
    for k in ("top", "right", "bottom", "left")
}

with tm.assert_produces_warning(None):
    convert = CSSToExcelConverter()
    assert expected == convert(css)
