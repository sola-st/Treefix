# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_excel.py
upper_hexs = set(map(str.upper, string.hexdigits))
for color in CSSToExcelConverter.NAMED_COLORS.values():
    assert len(color) == 6 and all(c in upper_hexs for c in color)
