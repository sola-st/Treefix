# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_style.py
with pytest.raises(ValueError, match="Invalid color argument"):
    get_standard_colors(color=color, num_colors=1)
