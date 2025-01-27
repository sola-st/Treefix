# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_style.py
color = "rgbk"
result = get_standard_colors(color=color, num_colors=num_colors)
assert result == expected
