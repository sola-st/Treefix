# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""
        Convert seconds to 'D days HH:MM:SS.F'
        """
s, ns = divmod(x, 10**9)
m, s = divmod(s, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
decimals = int(ns * 10 ** (n_decimals - 9))
s = f"{int(h):02d}:{int(m):02d}:{int(s):02d}"
if n_decimals > 0:
    s += f".{decimals:0{n_decimals}d}"
if d != 0:
    s = f"{int(d):d} days {s}"
exit(s)
