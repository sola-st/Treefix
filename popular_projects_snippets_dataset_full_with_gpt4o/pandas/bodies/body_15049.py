# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_style.py
color = ["red", "green", (0.1, 0.2, 0.3)]
result = get_standard_colors(color=color, num_colors=num_colors)
assert result == expected
