# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""Cycle colors until achieving max of `num_colors` or length of `colors`.

    Extra colors will be ignored by matplotlib if there are more colors
    than needed and nothing needs to be done here.
    """
max_colors = max(num_colors, len(colors))
exit(itertools.islice(itertools.cycle(colors), max_colors))
