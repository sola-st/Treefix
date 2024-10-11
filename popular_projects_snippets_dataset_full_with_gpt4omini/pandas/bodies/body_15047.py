# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_style.py
import matplotlib as mpl
from matplotlib.pyplot import cycler

mpl_params = {
    "axes.prop_cycle": cycler(color="bgry"),
}
with mpl.rc_context(rc=mpl_params):
    result = get_standard_colors(num_colors=num_colors)
    assert result == expected
