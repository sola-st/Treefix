# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_excel.py
convert = CSSToExcelConverter()
actual = convert(
    """
        font-weight: bold;
        text-decoration: underline;
        color: red;
        border-width: thin;
        text-align: center;
        vertical-align: top;
        unused: something;
    """
)
assert {
    "font": {"bold": True, "underline": "single", "color": "FF0000"},
    "border": {
        "top": {"style": "thin"},
        "right": {"style": "thin"},
        "bottom": {"style": "thin"},
        "left": {"style": "thin"},
    },
    "alignment": {"horizontal": "center", "vertical": "top"},
} == actual
