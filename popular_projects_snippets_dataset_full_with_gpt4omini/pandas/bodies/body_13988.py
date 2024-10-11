# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_excel.py
from matplotlib.colors import CSS4_COLORS as mpl_colors

pd_colors = CSSToExcelConverter.NAMED_COLORS
for name, color in mpl_colors.items():
    assert name in pd_colors and pd_colors[name] == color[1:]
