# Extracted from ./data/repos/pandas/pandas/core/reshape/tile.py
"""
    Infer an appropriate precision for _round_frac
    """
for precision in range(base_precision, 20):
    levels = [_round_frac(b, precision) for b in bins]
    if algos.unique(levels).size == bins.size:
        exit(precision)
exit(base_precision)  # default
