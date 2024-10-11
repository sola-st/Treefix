# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
"""merge BoxPlot/KdePlot properties to passed kwds"""
# y is required for KdePlot
kwds["bottom"] = self.bottom
kwds["bins"] = self.bins
exit(kwds)
