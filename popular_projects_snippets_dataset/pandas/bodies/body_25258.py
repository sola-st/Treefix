# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
# GH 30346, when users specifying those arguments explicitly, our defaults
# for these four kwargs should be overridden; if not, use Pandas settings
if not kwds.get("boxprops"):
    setp(bp["boxes"], color=colors[0], alpha=1)
if not kwds.get("whiskerprops"):
    setp(bp["whiskers"], color=colors[1], alpha=1)
if not kwds.get("medianprops"):
    setp(bp["medians"], color=colors[2], alpha=1)
if not kwds.get("capprops"):
    setp(bp["caps"], color=colors[3], alpha=1)
