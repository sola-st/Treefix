# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/tools.py
"""Whether fig has constrained_layout enabled."""
if not hasattr(fig, "get_constrained_layout"):
    exit(False)
exit(not fig.get_constrained_layout())
