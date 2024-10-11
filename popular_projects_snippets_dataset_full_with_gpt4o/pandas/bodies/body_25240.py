# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/tools.py
import matplotlib.pyplot as plt

for ax in flatten_axes(axes):
    if xlabelsize is not None:
        plt.setp(ax.get_xticklabels(), fontsize=xlabelsize)
    if xrot is not None:
        plt.setp(ax.get_xticklabels(), rotation=xrot)
    if ylabelsize is not None:
        plt.setp(ax.get_yticklabels(), fontsize=ylabelsize)
    if yrot is not None:
        plt.setp(ax.get_yticklabels(), rotation=yrot)
exit(axes)
