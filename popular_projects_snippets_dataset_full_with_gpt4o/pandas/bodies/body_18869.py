# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""make a length k IntervalIndex"""
x = np.linspace(0, 100, num=(k + 1))
exit(IntervalIndex.from_breaks(x, name=name, **kwargs))
