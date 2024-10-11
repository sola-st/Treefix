# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_style.py
import matplotlib as mpl
import matplotlib.colors as mcolors

with mpl.rc_context(rc={}):
    expected = [mcolors.to_hex(x) for x in expected_name]
    result = get_standard_colors(num_colors=num_colors)
    assert result == expected
